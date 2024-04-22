import os
import json
from openai import AzureOpenAI
    
AZURE_OPENAI_API_KEY="bf6dcf9ed1e445ec97782fbcd2c17d1d"
AZURE_OPENAI_ENDPOINT="https://teammetaprofiler.openai.azure.com/"
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,  
    api_version="2024-02-15-preview",
    azure_endpoint = AZURE_OPENAI_ENDPOINT
    )

    

# Create an assistant
assistant = client.beta.assistants.create(
    name="Data Insight",
    instructions=f"You are a helpful AI assistant who makes interesting visualizations based on data." ,
    tools=[{"type": "code_interpreter"}],
    model="MetaProfiler" #You must replace this value with the deployment name for your model.
)

print(assistant.model_dump_json(indent=2))

assistant.id="asst_xXXATIfFJEarBezhQ2Pxc9kI"