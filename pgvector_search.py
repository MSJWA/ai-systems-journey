import psycopg2
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()
db_password = os.getenv("POSTGRES_PASSWORD")

conn = psycopg2.connect(
    host="127.0.0.1",
    port="5433",
    dbname="postgres",
    user="postgres",
    password=db_password
)
cursor = conn.cursor()

model = SentenceTransformer('all-MiniLM-L6-v2')

question = "What's the French capital city?"
question_embedding = model.encode(question).tolist()

cursor.execute(
    "SELECT content FROM documents ORDER BY embedding <-> %s::vector LIMIT 1",
    (question_embedding,)
)
result = cursor.fetchone()
print("Best match:", result[0])

cursor.close()
conn.close()