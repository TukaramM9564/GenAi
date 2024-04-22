from openai import OpenAI
from GenAicode01 import OPENAI_API_KEY
client = OpenAI(
    api_key=OPENAI_API_KEY)

response=client.files.retrieve("file-829GgdqMpNl3o5QLxSPmFaQQ")

result=response.json()
print(result)
