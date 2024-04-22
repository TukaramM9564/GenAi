from openai import OpenAI
from GenAicode01 import OPENAI_API_KEY
client = OpenAI(
    api_key=OPENAI_API_KEY)



content = client.files.content("file-829GgdqMpNl3o5QLxSPmFaQQ")

result=content.json()
print(result)

#Not allowed to download files of purpose: assistants,user_data