import register_tools

from metrics import (
    increment_request,
    increment_tool
)

from tool_router import (
    select_tools
)

from mcp_client import (
    execute_tool as mcp_execute
)


def execute_tool(question):

    # Total request count
    increment_request()

    tools = select_tools(
        question
    )

    print(
        f"\nTOOLS SELECTED: {tools}"
    )

    results = []

    for tool_name in tools:

        # Tool usage count
        increment_tool(
            tool_name
        )

        result = mcp_execute(
            tool_name,
            question
        )

        if result:

            results.append(
                f"{tool_name.upper()}:\n{result}"
            )

    if not results:

        return "No tool results."

    return "\n\n".join(
        results
    )