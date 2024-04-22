import os
from openai import AzureOpenAI
import io
import time
from datetime import datetime
from pathlib import Path
from typing import Iterable

from openai import AzureOpenAI
from openai.types import FileObject
from openai.types.beta.threads.message_content_image_file import MessageContentImageFile
from openai.types.beta.threads.messages import MessageFile
from PIL import Image
AZURE_OPENAI_API_KEY="bf6dcf9ed1e445ec97782fbcd2c17d1d"
AZURE_OPENAI_ENDPOINT="https://teammetaprofiler.openai.azure.com/"
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,  
    api_version="2024-02-01",
    azure_endpoint = AZURE_OPENAI_ENDPOINT
    )
    
deployment_name='sampleprofiler' #This will correspond to the custom name you chose for your deployment when you deployed a model. Use a gpt-35-turbo-instruct deployment. 
    
# Send a completion call to generate an answer
print('Sending a test completion job')
start_phrase = 'Write a tagline for an ice cream shop. '
response = client.completions.create(model=deployment_name, prompt=start_phrase, max_tokens=10)
print(start_phrase+response.choices[0].text)