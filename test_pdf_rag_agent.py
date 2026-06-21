from tools.pdf_search import (
    load_pdf_to_vectorstore
)

from agents.pdf_rag_agent import (
    pdf_rag_agent
)

load_pdf_to_vectorstore(
    "data/sample.pdf"
)

print(
    pdf_rag_agent(
        "What is self-attention?"
    )
)