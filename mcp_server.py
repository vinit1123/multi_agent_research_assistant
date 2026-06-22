from tool_registry import get_all_tools


def list_tools():

    tools = get_all_tools()

    result = []

    for name, data in tools.items():

        result.append(
            {
                "name": name,
                "description": data["description"],
                "takes_input": data["takes_input"],
                "input_type": data["input_type"]
            }
        )

    return result


def call_tool(
    tool_name,
    *args,
    **kwargs
):

    tools = get_all_tools()

    if tool_name not in tools:

        return f"Tool '{tool_name}' not found"

    tool = tools[tool_name]

    func = tool["func"]

    takes_input = tool.get(
        "takes_input",
        True
    )

    # Memory tool jaisa tool
    if not takes_input:

        return func()

    # Calculator, Weather, Web Search, PDF Search
    return func(
        *args,
        **kwargs
    )