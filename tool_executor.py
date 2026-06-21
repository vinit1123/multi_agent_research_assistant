from tool_router import select_tool

from tools.calculator import calculator
from tools.web_search import web_search

from memory_manager import (
    search_memory,
    show_all_memories
)


def execute_tool(question):

    tool = select_tool(question)

    print(f"\nTOOL SELECTED: {tool}")

    # -------------------
    # Calculator
    # -------------------

    if tool == "calculator":

        return calculator(
            question
        )

    # -------------------
    # Memory
    # -------------------

    elif tool == "memory":

        memories = show_all_memories()

        if not memories:
            return "No memories found."

        return "\n".join(
            memories
        )

    # -------------------
    # Web Search
    # -------------------

    elif tool == "web_search":

        results = web_search(
            question,
            max_results=2
        )

        if not results:
            return "No search results found."

        formatted = []

        for r in results:

            formatted.append(
                f"Title: {r['title']}\n"
                f"Content: {r['body']}"
            )

        return "\n\n".join(
            formatted
        )

    # -------------------
    # Fallback
    # -------------------

    return "No tool found"