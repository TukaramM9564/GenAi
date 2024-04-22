from openai import AzureOpenAI
import json

AZURE_OPENAI_API_KEY="bf6dcf9ed1e445ec97782fbcd2c17d1d"
AZURE_OPENAI_ENDPOINT="https://teammetaprofiler.openai.azure.com/"
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,  
    api_version="2024-02-01",
    azure_endpoint = AZURE_OPENAI_ENDPOINT
    )
    
deployment_name='sampleprofiler' 
response=client.files.create(
  file=open(r"C:\Users\TSATYAWA\Downloads\customers_yourgpt.jsonl", "rb"),
  purpose="fine-tune"
)

result=response.model_dump_json()
print(result)

#id = file-829GgdqMpNl3o5QLxSPmFaQQ