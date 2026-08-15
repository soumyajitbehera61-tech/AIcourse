import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
#structure it
from pydantic import BaseModel
class ticket(BaseModel):
    name:str
    email:str
    issue:str
    contact_number:int
schema=ticket.model_json_schema()
response_format={
    "type":"json_object"
}
system_prompt=f"""
extract the personal information from the text based on the following schema and  give the  json output: {schema}
"""
message_system={
    "role":"system",
    "content":system_prompt
}
text="Hello, my name is  soumyajit.i am from odisha.i have an iphone which is not working.my email is  soumyya@gmail.com.my contact number is 456378."
prompt=f""" This is a customer ticket. Please extract the following information from the text:{text}"""



message={
 "role": role,
 "content": prompt
    }
messages=[message_system,message]
response=client.chat.completions.create(model=model, messages=messages,response_format=response_format)

answer=response.choices[0].message.content
print(answer)
# isko padhte kaise hai
import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=ticket(**data_file)


# inko pass kr sakte hai aage!
print(ticket.name)
print(ticket.email)
print(ticket.issue)
