from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def supervisor(question: str):

    prompt = f"""
You are a routing agent.

Choose ONLY one route:

research
summary
writer
chat

Rules:
- Current events, news, facts, technologies, research topics -> research
- Summarize something -> summary
- Write blog/article/report -> writer
- Greetings and casual conversation -> chat

Question:
{question}

Return ONLY one word:
research
summary
writer
chat
"""

    response = llm.invoke(prompt)

    route = response.content.strip().lower()

    print("\nRAW ROUTE:", route)

    if "research" in route:
        return "research"

    if "summary" in route:
        return "summary"

    if "writer" in route:
        return "writer"

    return "chat"