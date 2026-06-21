from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def select_tool(question):

    q = question.lower()

    # Calculator

    if any(
        op in q
        for op in ["+", "-", "*", "/", "="]
    ):
        return "calculator"

    # Memory

    if any(
        word in q
        for word in [
            "about me",
            "remember",
            "my name",
            "what do you know"
        ]
    ):
        return "memory"

    # Fallback to LLM

    response = llm.invoke(
        f"""
Select tool:

web_search
calculator
memory

Question:
{question}

Return only tool name.
"""
    )

    tool = response.content.strip().lower()

    # print("RAW TOOL:", tool)

    return tool