from openai import OpenAI
from GenAicode01 import OPENAI_API_KEY
import os
from openai import AzureOpenAI,images

AZURE_OPENAI_API_KEY="bf6dcf9ed1e445ec97782fbcd2c17d1d"
AZURE_OPENAI_ENDPOINT="https://teammetaprofiler.openai.azure.com/"
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,  
    api_version="2024-02-15-preview",
    azure_endpoint = AZURE_OPENAI_ENDPOINT
    )
    
deployment_name='MetaProfiler' 



content = client.files.content("assistant-CQe40B6xs2oIWPYHyBo3tuc5")
image= content.write_to_file(r"C:\Users\TSATYAWA\Downloads\dark_sine.png")
print(image)

# Display the image in the default image viewer
# image = images.open("dark_sine.png")
# image.show()

#result=content.json()


#Not allowed to download files of purpose: assistants,user_data