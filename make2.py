import openai
from openai import OpenAI, api_key


with open("apikey","r") as f:
  my_api_key = f.read()
  client = OpenAI(api_key=my_api_key[0:-1])
  print(client.api_key)
  completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
          {"role": "user", "content": "write a haiku about ai"}
      ]
  )

