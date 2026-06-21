TOOLS = {}

def register_tool(
    name,
    description,
    func,
    takes_input=True,
    input_type="text"
):

    TOOLS[name] = {
        "description": description,
        "func": func,
        "takes_input": takes_input,
        "input_type": input_type
    }


def get_all_tools():
    return TOOLS