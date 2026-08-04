import json
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Step 1: the real Python function the agent can call
def add_numbers(a, b):
    return a + b

# Step 2: describe that function to the LLM, in a structured format it understands
tools = [
    {
        "type": "function",
        "function": {
            "name": "add_numbers",
            "description": "Adds two numbers together",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    }
]

# Step 3: ask the LLM something that requires using the tool
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "What's the capital of France?"}],
    tools=tools
)

# Step 4: check if the LLM wants to call the tool
message = response.choices[0].message

if message.tool_calls:
    tool_call = message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    result = add_numbers(args["a"], args["b"])
    print(f"The LLM asked me to add {args['a']} + {args['b']}, result: {result}")
else:
    print(message.content)