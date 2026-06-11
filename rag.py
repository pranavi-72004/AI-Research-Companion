import numpy as np
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def create_chunks(text):
    chunk_size = 500
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

def get_embedding(text):
    result = genai.embed_content(
        model="models/embedding-001",
        content=text
    )
    return np.array(result["embedding"])

def build_vector_store(text):
    chunks = create_chunks(text)
    embeddings = [get_embedding(chunk) for chunk in chunks]
    return np.array(embeddings), chunks

def search_chunks(question, index, chunks):
    question_embedding = get_embedding(question)

    # Calculate similarity scores
    similarities = []
    for emb in index:
        score = np.dot(question_embedding, emb) / (
            np.linalg.norm(question_embedding) * np.linalg.norm(emb)
        )
        similarities.append(score)

    # Get top 3 most relevant chunks
    top_indices = np.argsort(similarities)[-3:][::-1]
    relevant_chunks = [chunks[i] for i in top_indices]

    return "\n".join(relevant_chunks)