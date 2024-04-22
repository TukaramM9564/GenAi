import os
import json
from openai import AzureOpenAI
import time


AZURE_OPENAI_API_KEY="bf6dcf9ed1e445ec97782fbcd2c17d1d"
AZURE_OPENAI_ENDPOINT="https://teammetaprofiler.openai.azure.com/"
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,  
    api_version="2024-02-15-preview",
    azure_endpoint = AZURE_OPENAI_ENDPOINT
    )

# Create a thread
thread = client.beta.threads.create()
#print(thread)


# Add a user question to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="as you wish"
)

#List Thread Messages
thread_messages = client.beta.threads.messages.list(thread.id)
#print(thread_messages.model_dump_json(indent=2))


#RunThread
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id="asst_u26AFa9qKZZOPygoxeft5C1Y",
  #instructions="New instructions" #You can optionally provide new instructions but these will override the default instructions
)


# Retrieve the status of the run
run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)


status=run.status
print(status)

import time
from IPython.display import clear_output

start_time = time.time()

status = run.status

while status not in ["completed", "cancelled", "expired", "failed"]:
    time.sleep(5)
    run = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print("Elapsed time: {} minutes {} seconds".format(int((time.time() - start_time) // 60), int((time.time() - start_time) % 60)))
    status = run.status
    print(f'Status: {status}')
    clear_output(wait=True)


messages = client.beta.threads.messages.list(
  thread_id=thread.id
) 

print(f'Status: {status}')
print("Elapsed time: {} minutes {} seconds".format(int((time.time() - start_time) // 60), int((time.time() - start_time) % 60)))
#print(messages.model_dump_json(indent=2))

#Once the run status indicates successful completion, you can list the contents of the thread again to retrieve the model's and any tools response:

messages = client.beta.threads.messages.list(
thread_id=thread.id
)

#print(messages.model_dump_json(indent=2))

#We had requested that the model generate an image of a sine wave. In order to download the image, we first need to retrieve the images file ID.
#Retrive File.id
data = json.loads(messages.model_dump_json(indent=2))  # Load JSON data into a Python object
#image_file_id = data['data'][0]['content'][0]['image_file']['file_id']

#print("image_file_id",image_file_id)  # Outputs: assistant-1YGVTvNzc2JXajI5JU9F0HMD

# Add a new user question to the thread
# message = client.beta.threads.messages.create(
#     thread_id=thread.id,
#     role="user",
#     content="give me sql query for the same"
# )

# run = client.beta.threads.runs.create(
#   thread_id=thread.id,
#   assistant_id="asst_u26AFa9qKZZOPygoxeft5C1Y",
#   #instructions="New instructions" #You can optionally provide new instructions  but these will override the default instructions
# )

# # Retrieve the status of the run
# run = client.beta.threads.runs.retrieve(
#   thread_id=thread.id,
#   run_id=run.id
# )

# status = run.status
# print(status)

# messages = client.beta.threads.messages.list(
#   thread_id=thread.id
# )

# print(messages.model_dump_json(indent=2))


#To extract only the response to our latest question:
data = json.loads(messages.model_dump_json(indent=2))
code = data['data'][0]['content'][0]['text']['value']
print(code)

