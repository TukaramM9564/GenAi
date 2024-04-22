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
  assistant_id="asst_p6kGTQnJlgMKvsfWDz1J9vkb",
  file_id=file_id
)
assistant_Result=assistant_file.model_dump_json()






#file.id = assistant-J0LdFkepbvxLiacM6yDfWvgN