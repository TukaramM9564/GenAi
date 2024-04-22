from openai import OpenAI
import os

OPENAI_API_KEY="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"
# # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# # if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
    api_key=OPENAI_API_KEY)




