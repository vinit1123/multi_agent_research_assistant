from langchain_ollama import ChatOllama
from tool_discovery import get_tool_descriptions
from tool_registry import get_all_tools

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


def select_tools(question):

    q = question.lower()

    tools = []

    # Calculator

    if any(
        op in q
        for op in ["+", "-", "*", "/", "="]
    ):
        tools.append(
            "calculator"
        )

    # Memory

    if any(
        word in q
        for word in [
            "about me",
            "remember",
            "my name",
            "who am i",
            "what do you know"
        ]
    ):
        tools.append(
            "memory"
        )

    # Weather

    if "weather" in q:
        tools.append(
            "weather"
        )

    # News / Search

    if any(
        x in q
        for x in [
            "news",
            "latest",
            "search"
        ]
    ):
        tools.append(
            "web_search"
        )

    # Nothing matched

    if tools:
        return list(set(tools))

    # LLM Fallback

    tool_names = list(
        get_all_tools().keys()
    )

    prompt = f"""
Available tools:

{tool_names}

Question:
{question}

Return only matching tool names.

Example:
weather,web_search
"""

    response = llm.invoke(
        prompt
    )

    result = response.content.lower()

    found = []

    for tool in tool_names:

        if tool in result:
            found.append(tool)

    if found:
        return found

    return ["web_search"]