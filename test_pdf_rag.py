import register_tools

from tools.pdf_search import (
    load_pdf_to_vectorstore,
    pdf_search_tool
)

print(
    load_pdf_to_vectorstore(
        "data/sample.pdf"
    )
)

print("\n" + "="*50 + "\n")

print(
    pdf_search_tool(
        "attention mechanism"
    )
)