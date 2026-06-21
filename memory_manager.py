import os

from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# ------------------------
# Embeddings
# ------------------------

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# ------------------------
# FAISS DB Path
# ------------------------

DB_PATH = "faiss_memory"

# ------------------------
# Load Existing Memory
# ------------------------

if os.path.exists(DB_PATH):

    vectorstore = FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    print("\nFAISS MEMORY LOADED")

else:

    vectorstore = FAISS.from_texts(
        ["init"],
        embeddings
    )

    vectorstore.save_local(
        DB_PATH
    )

    print("\nNEW FAISS MEMORY CREATED")

# ------------------------
# Check Duplicate Memory
# ------------------------

def memory_exists(text):

    docs = vectorstore.similarity_search(
        text,
        k=1
    )

    if not docs:
        return False

    existing = docs[0].page_content.lower().strip()
    incoming = text.lower().strip()

    return existing == incoming

# ------------------------
# Save Memory
# ------------------------

def save_long_term_memory(text):

    text = text.strip()

    if not text:
        return

    # Skip duplicates
    if memory_exists(text):

        print(
            f"MEMORY ALREADY EXISTS: {text}"
        )

        return

    doc = Document(
        page_content=text
    )

    vectorstore.add_documents(
        [doc]
    )

    vectorstore.save_local(
        DB_PATH
    )

    print(
        f"MEMORY SAVED: {text}"
    )

# ------------------------
# Search Memory
# ------------------------

def search_memory(query):

    docs = vectorstore.similarity_search(
        query,
        k=5
    )

    filtered = []

    for doc in docs:

        if doc.page_content in [
            "init",
            "Memory Initialized"
        ]:
            continue

        filtered.append(doc)

    return filtered

# ------------------------
# Show All Memories
# ------------------------

def show_all_memories():

    docs = vectorstore.similarity_search(
        "",
        k=100
    )

    memories = []

    for doc in docs:

        if doc.page_content == "init":
            continue

        if doc.page_content not in memories:
            memories.append(
                doc.page_content
            )

    return memories