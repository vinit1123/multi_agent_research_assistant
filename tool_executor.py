import register_tools

from tool_router import select_tool

from mcp_client import (
    execute_tool as mcp_execute_tool,
    discover_tools
)


def execute_tool(question):

    tool_name = select_tool(question)

    print(
        f"\nTOOL SELECTED: {tool_name}"
    )

    tools = discover_tools()

    tool_info = None

    for tool in tools:

        if tool["name"] == tool_name:

            tool_info = tool
            break

    if not tool_info:
        return "Tool not found"

    # Tool needs input

    if tool_info["takes_input"]:

        result = mcp_execute_tool(
            tool_name,
            question
        )

    # Tool does not need input

    else:

        result = mcp_execute_tool(
            tool_name
        )

    # Format web search

    if (
        tool_name == "web_search"
        and isinstance(result, list)
    ):

        formatted = []

        for r in result:

            formatted.append(
                f"Title: {r['title']}\n"
                f"Content: {r['body']}"
            )

        return "\n\n".join(
            formatted
        )

    # Format memory

    if (
        tool_name == "memory"
        and isinstance(result, list)
    ):

        return "\n".join(result)

    return result