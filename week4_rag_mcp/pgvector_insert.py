import psycopg2
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()
db_password = os.getenv("POSTGRES_PASSWORD")
print(f"Password loaded as: '{db_password}'")

conn = psycopg2.connect(
    host="localhost",
    port="5433",
    dbname="postgres",
    user="postgres",
    password=db_password
)
cursor = conn.cursor()

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "The capital of France is Paris.",
    "Python is a popular programming language for AI.",
    "The Eiffel Tower was built in 1889.",
    "FastAPI is used to build APIs in Python."
]

for doc in documents:
    embedding = model.encode(doc).tolist()
    cursor.execute(
        "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
        (doc, embedding)
    )

conn.commit()
cursor.close()
conn.close()
print("Documents inserted.")