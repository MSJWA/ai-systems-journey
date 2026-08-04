from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "The capital of France is Paris.",
    "Python is a popular programming language for AI.",
    "The Eiffel Tower was built in 1889.",
    "FastAPI is used to build APIs in Python."
]

doc_embeddings = model.encode(documents)

def real_retrieve(question, documents, doc_embeddings):
    question_embedding = model.encode([question])[0]

    similarities = np.dot(doc_embeddings, question_embedding)

    best_index = np.argmax(similarities)
    return documents[best_index]

question = "What's the French capital city?"
print(real_retrieve(question, documents, doc_embeddings))