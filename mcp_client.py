from mcp_server import (
    list_tools,
    call_tool
)


def discover_tools():

    return list_tools()


def execute_tool(
    tool_name,
    *args,
    **kwargs
):

    return call_tool(
        tool_name,
        *args,
        **kwargs
    )