from langchain_ollama import ChatOllama
from tool_executor import execute_tool
from tool_router import select_tool

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def tool_agent(question):

    print("STEP 1")

    tool = select_tool(question)

    

    tool_result = execute_tool(question)

    print("STEP 2")
    print(tool_result)

    # -------------------
    # Calculator
    # -------------------

    if tool == "calculator":

        return str(tool_result)

    # -------------------
    # Memory
    # -------------------

    elif tool == "memory":

        return f"""
Stored Information:

{tool_result}
"""

    # -------------------
    # Web Search
    # -------------------

    elif tool == "web_search":

        prompt = f"""
You are a research assistant.

Search Results:
{tool_result}

Instructions:
- Summarize the search results.
- Mention key points only.
- Be concise.
- Do not invent facts.
"""

        print("STEP 3")

        response = llm.invoke(prompt)

        print("STEP 4")

        return response.content

    return "No answer generated."