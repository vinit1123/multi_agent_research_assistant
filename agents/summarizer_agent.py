from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    base_url="http://127.0.0.1:11434",
    temperature=0
)

def summarizer_agent(text):

    prompt = f"""
Create a professional summary.

Return:

1. Executive Summary

2. Key Findings

3. Important Points

Content:

{text}
"""

    response = llm.invoke(prompt)

    return response.content