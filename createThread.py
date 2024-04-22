import os
import json
from openai import AzureOpenAI
from createAssistant import client,assistant

# Create a thread
thread = client.beta.threads.create()
#print(thread)
thread.id="thread_f9U3aszwwxG3y3CsHbxmevs1"

# Add a user question to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Create a visualization of a sinewave"
)
assistant.id="asst_xXXATIfFJEarBezhQ2Pxc9kI"
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  #instructions="New instructions" #You can optionally provide new instructions but these will override the default instructions
)

print(run)
run.id="run_OKjOlRHNwGPuFO2uqVykJ2Dh"