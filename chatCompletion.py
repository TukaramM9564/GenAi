from openai import OpenAI
# from GenAicode01 import OPENAI_API_KEY
import json
OPENAI_API_KEY="bf6dcf9ed1e445ec97782fbcd2c17d1d"
client = OpenAI(
    api_key=OPENAI_API_KEY)




response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write a tagline for an ice cream shop."
)

result=response.json()
print(result)