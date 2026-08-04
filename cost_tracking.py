import os
from groq import Groq
from dotenv import load_dotenv
import logging

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

logging.basicConfig(
    filename="cost_tracking.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    max_tokens=100,
    messages=[{"role": "user", "content": "Say hello in one sentence."}]
)

usage = response.usage
print(f"Prompt tokens: {usage.prompt_tokens}")
print(f"Completion tokens: {usage.completion_tokens}")
print(f"Total tokens: {usage.total_tokens}")

logging.info(f"model=llama-3.3-70b-versatile prompt_tokens={usage.prompt_tokens} completion_tokens={usage.completion_tokens} total_tokens={usage.total_tokens}")