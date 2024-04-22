import os
from openai import AzureOpenAI
import json
from IPython.display import display

AZURE_OPENAI_API_KEY="bf6dcf9ed1e445ec97782fbcd2c17d1d"
AZURE_OPENAI_ENDPOINT="https://teammetaprofiler.openai.azure.com/"
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,  
    api_version="2024-02-15-preview",
    azure_endpoint = AZURE_OPENAI_ENDPOINT
    )
print("step1")
assistant_id="asst_GY8WvHMkkAq0a972nNaDNM3O"
def show_json(obj):
    display(json.loads(obj.model_dump_json()))

# Create an assistant
from openai import AzureOpenAI
import json

AZURE_OPENAI_API_KEY="bf6dcf9ed1e445ec97782fbcd2c17d1d"
AZURE_OPENAI_ENDPOINT="https://teammetaprofiler.openai.azure.com/"
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,  
    api_version="2024-02-15-preview",
    azure_endpoint = AZURE_OPENAI_ENDPOINT
    )
    
deployment_name='MetaProfiler' 
response=client.files.create(
  file=open(r"C:\Users\TSATYAWA\Downloads\username.csv", "rb"),
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






#file.id = assistant-J0LdFkepbvxLiacM6yDfWvgN
# show_json(assistant)
print("step2")
#Next create thread
thread = client.beta.threads.create()

#Set the question to ask
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="tell me about username file"
)

#show_json(message)
print("step3")
#function to wait for run to complete
import time
def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run



#Create the run using threads
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant_id,
)
#show_json(run)


#run the code
run = wait_on_run(run, thread)
#show_json(run)

#list all messages
messages = client.beta.threads.messages.list(thread_id=thread.id)
#show_json(messages)

#ask for model to explain
# Create a message to append to our thread
message = client.beta.threads.messages.create(
    thread_id=thread.id, role="user", content="does it contain corrupted data if yes remove it "
)
# Execute our run
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant_id,
)
# Wait for completion
wait_on_run(run, thread)

# Retrieve all the messages added after our last user message
messages = client.beta.threads.messages.list(
    thread_id=thread.id, order="asc", after=message.id
)

#show_json(messages)

#display the output
print(messages.data[0].content[0].text.value)

# data = json.loads(messages.model_dump_json(indent=2))  
# image_file_id = data['data'][0]['content'][0]['image_file']['file_id']

# content = client.files.content("assistant-cbDkVcN5J73rgdHByNLO82j1")
# image= content.write_to_file(r"C:\Users\TSATYAWA\Downloads\dark_sine.png")