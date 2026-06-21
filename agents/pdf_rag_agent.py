from langchain_ollama import ChatOllama

from tools.pdf_search import pdf_search_tool

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def pdf_rag_agent(question):

    context = pdf_search_tool(
        question
    )

    prompt = f"""
You are a PDF question-answering assistant.

Question:
{question}

Relevant Context:
{context}

Instructions:
- Answer using only the context.
- If answer is not present, say:
  "Information not found in PDF."
- Be concise.
"""

    response = llm.invoke(
        prompt
    )

    return response.content