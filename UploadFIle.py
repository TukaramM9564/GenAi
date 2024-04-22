from openai import OpenAI
from GenAicode01 import OPENAI_API_KEY
import json
client = OpenAI(
    api_key=OPENAI_API_KEY)

response=client.files.create(
  file=open(r"C:\Users\TSATYAWA\Downloads\customers_yourgpt.jsonl", "rb"),
  purpose="assistants"
)

result=response.json()
result=json.loads(result)

print(result['id'])
#id = file-829GgdqMpNl3o5QLxSPmFaQQ