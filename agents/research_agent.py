from tools.web_search import web_search
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def research_agent(question):

    print("\nQUESTION:")
    print(question)

    results = web_search(
        question,
        max_results=2
    )

    print("\nSEARCH RESULTS:\n")
    print(results)

    print("\nTOTAL:", len(results))

    if not results:
        return "No search results found."

    context = "\n\n".join(
    f"Title: {r['title']}\n"
    f"Content: {r['body'][:200]}"
    for r in results
)
    

    print("\nCONTEXT CREATED")

    prompt = f"""
You are an expert research assistant.

Use ONLY the search results provided.

Question:
{question}

Search Results:
{context}

Instructions:
- Give a concise answer.
- Use information from the search results.
- If information is insufficient, say so.
"""

    print("\nBEFORE LLM CALL")
    print("\nPROMPT LENGTH:", len(prompt))
    response = llm.invoke(prompt)

    print("\nAFTER LLM CALL")

    print("\nRAW RESPONSE:")
    print(response)

    return response.content