from mcp_client import discover_tools

def get_tool_descriptions():

    tools = discover_tools()

    output = []

    for tool in tools:

        output.append(
            f"{tool['name']}: {tool['description']}"
        )

    return "\n".join(output)

