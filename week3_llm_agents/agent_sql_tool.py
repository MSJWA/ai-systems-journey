import json
import sqlite3
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def find_user(name):
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    result = cursor.fetchone()
    connection.close()

    if result:
        return {"id": result[0], "name": result[1], "age": result[2]}
    else:
        return {"error": f"No user found with name {name}"}

tools = [
    {
        "type": "function",
        "function": {
            "name": "find_user",
            "description": "Looks up a user's information by their name",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "required": ["name"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Can you find Ali's info for me?"}],
    tools=tools
)

message = response.choices[0].message

if message.tool_calls:
    tool_call = message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    result = find_user(args["name"])
    print(result)
else:
    print(message.content)