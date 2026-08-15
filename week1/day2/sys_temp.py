import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY not found")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
messages_system={
    "role": "system",
    "content": "You are a product naming assistant."
}

messages = [
    {
        "role": "user",
        "content": "suggest me a fashion brand name that i  can name from my restaurant idea?.just answer in one line."
    }
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=2,
)

print(response.choices[0].message.content)