from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)