import os
from openai import AzureOpenAI
import json
from IPython.display import display,clear_output,Markdown,Image
import time

AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_ENDPOINT="https://team10.openai.azure.com/"
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,  
    api_version="2024-02-15-preview",
    azure_endpoint = AZURE_OPENAI_ENDPOINT
    )



#file upload to assistant
deployment_name='Metaprofiler'
def file_upload(path):
    assistant_id="asst_gMQEHLJ9gSl24QAGanhj5EYm" 
    response=client.files.create(
    file=open(path,"rb"),
    purpose="assistants"
    )

    result=response.model_dump_json()
    result=json.loads(result)
    file_id=result['id']

    assistant_file = client.beta.assistants.files.create(
    assistant_id=assistant_id,
    file_id=file_id
    )
    assistant_Result=assistant_file.model_dump_json()
    return assistant_Result

def Assistant_prompt(prompt):
    assistant_id="asst_gMQEHLJ9gSl24QAGanhj5EYm"
    #create a Thread
    thread=client.beta.threads.create()

   
    message=client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )

    #show the messages
    thread_messages=client.beta.threads.messages.list(thread.id)
    #print(thread_messages.model_dump_json(indent=2))

    #run Thread
    run=client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id
    )

    status=run.status

    while status not in ["completed","cancelled","expired","failed"]:
        time.sleep(2)
        run=client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
        status=run.status
        #print(f'status: {status}')
        clear_output(wait=True)

    #print(f'status :{status}')

    messages=client.beta.threads.messages.list(
        thread_id=thread.id
    )

    messages_json=json.loads(messages.model_dump_json())

    return messages_json


    # for item in reversed(messages_json['data']):
    #     for content in reversed(item['content']):
    #         if 'text' in content:
    #             print((content[0]['text']['value']))
    #         if 'image_file' in content:
    #             file_id=content['image_file']['file_id']
    #             file_content=client.files.content(file_id)
    #             image= file_content.write_to_file(r"C:\Users\TSATYAWA\Downloads\dark_sine.png")


            
