from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def create_chunks(text):

    chunk_size = 500

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])

    return chunks


def build_vector_store(text):

    chunks = create_chunks(text)

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(
        np.array(embeddings).astype("float32")
    )

    return index, chunks


def search_chunks(question, index, chunks):

    question_embedding = model.encode([question])

    distances, indices = index.search(
        np.array(question_embedding).astype("float32"),
        3
    )

    relevant_chunks = []

    for idx in indices[0]:
        relevant_chunks.append(
            chunks[idx]
        )

    return "\n".join(relevant_chunks)