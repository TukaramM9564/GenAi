import os
import json
from openai import AzureOpenAI
from createAssistant import client,assistant
from createAssistant import client,assistant
from createThread import thread,message,run

# Retrieve the status of the run


run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)

messages = client.beta.threads.messages.list(
  thread_id=thread.id
)

#print(messages.model_dump_json(indent=2))

data = json.loads(messages.model_dump_json(indent=2))  # Load JSON data into a Python object
print("data    =",data)
image_file_id = data['data'][0]['content'][0]['image_file']['file_id']

print(image_file_id)  # Outputs: assistant-1YGVTvNzc2JXajI5JU9F0HMD

# status = run.status
# print(status)