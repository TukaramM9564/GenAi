import os
import json
from openai import AzureOpenAI
from createAssistant import client,assistant
from createAssistant import client,assistant
from createThread import thread,message,run

# thread.id="thread_f9U3aszwwxG3y3CsHbxmevs1"
# run.id="run_OKjOlRHNwGPuFO2uqVykJ2Dh"

messages = client.beta.threads.messages.list(
  thread_id=thread.id
)

#print(messages.model_dump_json(indent=2))





messages = client.beta.threads.messages.list(
  thread_id=thread.id
)

print(messages.model_dump_json(indent=2))

data = json.loads(messages.model_dump_json(indent=2))  # Load JSON data into a Python object
image_file_id = data['data'][0]['content'][0]['image_file']['file_id']

print(image_file_id)  # Outputs: assistant-1YGVTvNzc2JXajI5JU9F0HMD

content = client.files.content(image_file_id)

image= content.write_to_file("sinewave.png")


# Retrieve the message object
message = client.beta.threads.messages.retrieve(
  thread_id="thread_f9U3aszwwxG3y3CsHbxmevs1",
  message_id="msg_nc24xtjkM68Kql9r3FOEGGO4"
)
# # Extract the message content
# message_content = message.content[0].text
# annotations = message_content.annotations
# citations = []

# # Iterate over the annotations and add footnotes
# for index, annotation in enumerate(annotations):
#     # Replace the text with a footnote
#     message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

#     # Gather citations based on annotation attributes
#     if (file_citation := getattr(annotation, 'file_citation', None)):
#         cited_file = client.files.retrieve(file_citation.file_id)
#         citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
#     elif (file_path := getattr(annotation, 'file_path', None)):
#         cited_file = client.files.retrieve(file_path.file_id)
#         citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
#         # Note: File download functionality not implemented above for brevity

# # Add footnotes to the end of the message before displaying to user
# message_content.value += '\n' + '\n'.join(citations)

#print(message_content.value)

