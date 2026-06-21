from langchain_ollama import ChatOllama

from tool_executor import execute_tool

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def tool_agent(question):

    # Execute tool through MCP
    tool_result = execute_tool(
        question
    )

    # Memory Tool
    if isinstance(tool_result, str) and (
        "My name is" in tool_result
        or "QA Lead" in tool_result
        or "GenAI Developer" in tool_result
    ):

        return (
            "Stored Information:\n\n"
            + tool_result
        )

    # Calculator Tool
    if (
        isinstance(tool_result, str)
        and tool_result.strip().isdigit()
    ):

        return tool_result

    # Web Search / Weather / Future Tools
    return tool_result