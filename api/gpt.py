from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv("../.env")

key = os.getenv("GPT_KEY")

client = OpenAI(api_key=key)

response = client.responses.create(
  model="gpt-4o-mini",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);