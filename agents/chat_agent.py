from langchain_ollama import ChatOllama

from memory_manager import (
    search_memory,
    save_long_term_memory
)

from memory import (
    get_formatted_memory,
    save_memory
)

from memory_classifier import (
    should_save_memory
)

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def chat_agent(question):

    # Short-term memory
    history = get_formatted_memory()

    # Long-term memory retrieval
    memories = search_memory(question)

    memory_context = "\n".join(
        doc.page_content
        for doc in memories
    )

    prompt = f"""
You are a helpful AI assistant.

Relevant Long-Term Memory:
{memory_context}

Conversation History:
{history}

Current User Message:
{question}

Instructions:
- Use long-term memory only if relevant.
- Use conversation history when relevant.
- Do not repeat memory unnecessarily.
- Answer the user's question directly.
- Be concise.
- Do not ask follow-up questions unless needed.
- Do not print Human: or Assistant:
"""

    response = llm.invoke(prompt)

    # Save to short-term memory
    save_memory(
        "user",
        question
    )

    save_memory(
        "assistant",
        response.content
    )

    # Save important information to long-term memory
    if should_save_memory(question):

        print(
            "\nSAVING TO LONG TERM MEMORY"
        )

        save_long_term_memory(
            question
        )

    return response.content