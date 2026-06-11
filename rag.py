import numpy as np
import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def create_chunks(text):
    chunk_size = 500
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

def get_embedding(text):
    result = client.models.embed_content(
        model="gemini-embedding-exp-03-07",
        contents=text
    )
    return np.array(result.embeddings[0].values)

def build_vector_store(text):
    chunks = create_chunks(text)
    embeddings = [get_embedding(chunk) for chunk in chunks]
    return np.array(embeddings), chunks

def search_chunks(question, index, chunks):
    question_embedding = get_embedding(question)
    similarities = []
    for emb in index:
        score = np.dot(question_embedding, emb) / (
            np.linalg.norm(question_embedding) * np.linalg.norm(emb)
        )
        similarities.append(score)
    top_indices = np.argsort(similarities)[-3:][::-1]
    relevant_chunks = [chunks[i] for i in top_indices]
    return "\n".join(relevant_chunks)