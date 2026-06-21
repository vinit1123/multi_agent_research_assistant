from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from pypdf import PdfReader

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vectorstore = None


def load_pdf_to_vectorstore(file_path):

    global vectorstore

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    chunks = []

    chunk_size = 1000

    for i in range(0, len(text), chunk_size):

        chunks.append(
            Document(
                page_content=text[i:i + chunk_size]
            )
        )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return f"{len(chunks)} chunks loaded"


def pdf_search_tool(query):

    global vectorstore

    if vectorstore is None:
        return "No PDF loaded."

    docs = vectorstore.similarity_search(
        query,
        k=3
    )

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )