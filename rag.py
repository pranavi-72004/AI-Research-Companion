def create_chunks(text):
    chunk_size = 500
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

def build_vector_store(text):
    chunks = create_chunks(text)
    return None, chunks

def search_chunks(question, index, chunks):
    question_words = question.lower().split()
    scored_chunks = []
    for chunk in chunks:
        chunk_lower = chunk.lower()
        score = sum(1 for word in question_words if word in chunk_lower)
        scored_chunks.append((score, chunk))
    scored_chunks.sort(reverse=True)
    top_chunks = [chunk for _, chunk in scored_chunks[:3]]
    return "\n".join(top_chunks)