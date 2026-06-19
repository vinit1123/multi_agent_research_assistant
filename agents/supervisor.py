from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def supervisor(question: str):

    q = question.lower()

    # Fast deterministic routing

    if any(word in q for word in [
        "latest",
        "news",
        "research",
        "current",
        "recent"
    ]):
        return "research"

    if any(word in q for word in [
        "summarize",
        "summary",
        "summarise"
    ]):
        return "summary"

    if any(word in q for word in [
        "write",
        "blog",
        "email",
        "article",
        "report"
    ]):
        return "writer"

    # Fallback to LLM

    prompt = f"""
Return ONLY one word:

research
summary
writer
chat

Question:
{question}
"""

    response = llm.invoke(prompt)

    route = response.content.strip().lower()

    if "research" in route:
        return "research"

    if "summary" in route:
        return "summary"

    if "writer" in route:
        return "writer"

    return "chat"