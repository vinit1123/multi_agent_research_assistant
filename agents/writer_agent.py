from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    base_url="http://127.0.0.1:11434",
    temperature=0
)

def writer_agent(text):

    prompt = f"""
You are a professional technical writer.

Create a well structured report.

Include:

1. Title

2. Introduction

3. Main Discussion

4. Conclusion

Content:

{text}
"""

    response = llm.invoke(prompt)

    return response.content