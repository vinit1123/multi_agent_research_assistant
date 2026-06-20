from tools.web_search import web_search
from langchain_ollama import ChatOllama
from memory_classifier import should_save_memory
from memory_manager import save_long_term_memory

from memory import (
    get_memory,
    get_formatted_memory,
    save_memory,
    is_followup
)

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def research_agent(question):

    # -------------------------
    # Follow-up Question Path
    # -------------------------

    if is_followup(question):

        history = get_formatted_memory()

        prompt = f"""
You are an expert AI assistant.

Previous Conversation:

{history}

Current Question:
{question}

Instructions:
- Continue the previous discussion.
- Use conversation history.
- Do NOT start a new topic.
- Do NOT print Human: or Assistant:
- Give a natural answer.
"""

        response = llm.invoke(prompt)

    if should_save_memory(question):

        print("\nSAVING TO LONG TERM MEMORY")

    save_long_term_memory(
        question
    )

    save_memory(
            "user",
            question
        )

    save_memory(
            "assistant",
            response.content
        )

    return response.content

    # -------------------------
    # Normal Research Path
    # -------------------------

    history = get_formatted_memory()

    print("\nQUESTION:")
    print(question)

    results = web_search(
        question,
        max_results=2
    )

    print("\nSEARCH RESULTS:\n")
    print(results)

    if not results:
        return "No search results found."

    context = "\n\n".join(
        f"Title: {r['title']}\n"
        f"Content: {r['body'][:200]}"
        for r in results
    )

    prompt = f"""
You are an expert research assistant.

Question:
{question}

Search Results:
{context}

Previous Conversation:
{history}

Instructions:
- Use the search results.
- Answer clearly.
- Be concise.
"""

    response = llm.invoke(prompt)

    save_memory(
        "user",
        question
    )

    save_memory(
        "assistant",
        response.content
    )

    return response.content