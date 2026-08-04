import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

documents = [
    "The capital of France is Paris.",
    "Python is a popular programming language for AI.",
    "The Eiffel Tower was built in 1889.",
    "FastAPI is used to build APIs in Python."
]

def simple_retrieve(question, documents):
    question_words = set(question.lower().split())
    best_doc = None
    best_score = 0

    for doc in documents:
        doc_words = set(doc.lower().split())
        overlap = len(question_words & doc_words)
        if overlap > best_score:
            best_score = overlap
            best_doc = doc

    return best_doc

question = "What is the capital of France?"
retrieved_doc = "FastAPI is used to build APIs in Python."

prompt = f"""Answer the question using only the context below.

Context: {retrieved_doc}

Question: {question}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)