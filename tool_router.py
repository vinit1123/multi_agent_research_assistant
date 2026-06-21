import register_tools

from langchain_ollama import ChatOllama

from tool_discovery import (
    get_tool_descriptions
)

from tool_registry import (
    get_all_tools
)

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


def select_tool(question):

    q = question.lower()

    # -------------------
    # Fast Rules
    # -------------------

    if any(
        op in q
        for op in ["+", "-", "*", "/", "="]
    ):
        return "calculator"

    if any(
        word in q
        for word in [
            "about me",
            "remember",
            "my name",
            "what do you know",
            "who am i"
        ]
    ):
        return "memory"

    # -------------------
    # Dynamic Tool Discovery
    # -------------------

    tools_description = get_tool_descriptions()

    available_tools = list(
        get_all_tools().keys()
    )

    tool_list = "\n".join(
        available_tools
    )

    prompt = f"""
You are a tool routing agent.

Available Tools:

{tools_description}

Valid Tool Names:

{tool_list}

Rules:
- Choose the single BEST tool.
- Return ONLY one tool name.
- Never invent a tool name.
- Never explain your answer.
- Output must exactly match one valid tool name.

Question:
{question}
"""

    response = llm.invoke(prompt)

    tool = response.content.strip().lower()

    # print("\nAVAILABLE TOOLS:")
    # print(available_tools)

    # print("\nRAW TOOL:")
    # print(tool)

    # -------------------
    # Validation
    # -------------------

    if tool in available_tools:
        return tool

    print(
        "\nINVALID TOOL -> FALLBACK TO web_search"
    )

    return "web_search"