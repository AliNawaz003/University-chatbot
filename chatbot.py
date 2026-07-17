import os
import json
import re

import chromadb
from sentence_transformers import SentenceTransformer

# -------------------------
# GLOBALS
# -------------------------
EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
DATASET_PATH = "Aror_Chatbot_Dataset_cleaned.json"
CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "university_chatbot"

model = None
collection = None


# -------------------------
# TEXT CLEANING
# -------------------------
def clean_text(text):
    text = str(text).replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# -------------------------
# SIMPLE CHUNKING (FASTER)
# -------------------------
def chunk_text(text, chunk_size=120):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        if len(chunk.split()) > 5:
            chunks.append(chunk)

    return chunks


# -------------------------
def initialize_rag():
    global model, collection

    if model is not None and collection is not None:
        return

    print("Loading model...")
    model = SentenceTransformer(EMBED_MODEL_NAME)

    print("Setting up database...")
    client = chromadb.Client()

    try:
        collection = client.get_collection(COLLECTION_NAME)
    except:
        collection = client.create_collection(name=COLLECTION_NAME)

    print("Loading dataset...")
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []
    ids = []

    for item in data:
        text = clean_text(item.get("text", ""))
        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            documents.append(chunk)
            ids.append(f"{item.get('id','doc')}_{i}")

    print("Creating embeddings...")
    embeddings = model.encode(documents).tolist()

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids
    )

    print("System ready!")

# -------------------------
# QUERY SYSTEM (FAST)
# -------------------------
def query_system(query, top_k=3):
    global model, collection

    if model is None or collection is None:
        initialize_rag()

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    return results["documents"][0]


# -------------------------
# CHATBOT FUNCTION
# -------------------------
def chatbot(user_query):
    results = query_system(user_query)

    if not results:
        return "No relevant information found. Try asking about admissions, faculty, or programs."

    answer = results[0]

    if len(results) > 1:
        related = "\n".join([f"- {r}" for r in results[1:]])
        return f"{answer}\n\nRelated:\n{related}"

    return answer