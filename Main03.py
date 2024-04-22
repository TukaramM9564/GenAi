import os
from openai import AzureOpenAI
import json
from IPython.display import display
import html
import io
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Iterable
import requests
from openai import AzureOpenAI
from openai.types import FileObject
from openai.types.beta import Thread
from openai.types.beta.threads import Run
from openai.types.beta.threads.message_content import MessageContent

from openai.types.beta.threads.message_content_image_file import MessageContentImageFile

from openai.types.beta.threads.message_content_text import MessageContentText

from openai.types.beta.threads.messages import MessageFile

from IPython.display import Image
from openai.types.beta.threads.messages import MessageFile

 

AZURE_OPENAI_API_KEY="bf6dcf9ed1e445ec97782fbcd2c17d1d"
AZURE_OPENAI_ENDPOINT="https://teammetaprofiler.openai.azure.com/"
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,  
    api_version="2024-02-15-preview",
    azure_endpoint = AZURE_OPENAI_ENDPOINT
    )



def upload_file(client: AzureOpenAI, path: str) -> FileObject:
    with Path(path).open("rb") as f:
        return client.files.create(file=f, purpose="assistants")
    
    

filePath = 'data/portfolio.csv'
assistant_files = []
assistant_files.append(upload_file(client, filePath))
file_ids = [file.id for file in assistant_files]

assistant = client.beta.assistants.create(
    name="Data Insight",
    instructions=f"You are a helpful AI assistant who makes interesting math questioning based on data." ,
    tools=[{"type": "code_interpreter"}],
    model="MetaProfiler",
    file_ids=file_ids,
)

thread = client.beta.threads.create()
def read_assistant_file(file_id:str):
    response_content = client.files.content(file_id)
    return response_content.read()


def print_messages(messages: Iterable[MessageFile]) -> None:
    message_list = []

    # Get all the messages till the last user message
    for message in messages:
        message_list.append(message)
        if message.role == "user":
            break

    # Reverse the messages to show the last user message first
    message_list.reverse()

    # Print the user or Assistant messages or images
    for message in message_list:
        for item in message.content:
            # Determine the content type
            if isinstance(item, MessageContentText):
                print(f"{message.role}:\n{item.text.value}\n")
                file_annotations = item.text.annotations
                if file_annotations:
                    for annotation in file_annotations:
                        file_id = annotation.file_path.file_id
                        content = read_assistant_file(file_id)
                        print(f"Annotation Content:\n{str(content)}\n")
            elif isinstance(item, MessageContentImageFile):
                # Retrieve image from file id                
                data_in_bytes = read_assistant_file(item.image_file.file_id)
                # Convert bytes to image
                readable_buffer = io.BytesIO(data_in_bytes)
                image = Image.open(readable_buffer)
                # Resize image to fit in terminal
                width, height = image.size
                image = image.resize((width // 2, height // 2), Image.LANCZOS)
                # Display image
                image.show()


def process_prompt(prompt: str) -> None:
    client.beta.threads.messages.create(thread_id=thread.id, role="user", content=prompt)
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions="Please address the user as Jane Doe. The user has a premium account. Be assertive, accurate, and polite. Ask if the user has further questions. "
        + "The current date and time is: "
        + datetime.now().strftime("%x %X")
        + ". ",
    )
    print("processing ...")
    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run.status == "completed":
            # Handle completed
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            print_messages(messages)
            break
        if run.status == "failed":
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            answer = messages.data[0].content[0].text.value
            print(f"Failed User:\n{prompt}\nAssistant:\n{answer}\n")
            # Handle failed
            break
        if run.status == "expired":
            # Handle expired
            print(run)
            break
        if run.status == "cancelled":
            # Handle cancelled
            print(run)
            break
        if run.status == "requires_action":
            # Handle function calling and continue processing
            pass
        else:
            time.sleep(5)

process_prompt("Based on the provided portfolio, what investments do I own?")