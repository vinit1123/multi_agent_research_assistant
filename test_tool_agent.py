from langchain_ollama import ChatOllama

from tool_executor import execute_tool

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def tool_agent(question):

    tool_result = execute_tool(
        question
    )

    print("\nTOOL RESULT:")
    print(tool_result)

    prompt = f"""
You are a factual assistant.

User Question:
{question}

Available Information:
{tool_result}

Rules:
1. Use ONLY the Available Information.
2. Do NOT use outside knowledge.
3. Do NOT invent facts.
4. If information is insufficient, say:
   "The available information is insufficient."
5. Give a direct answer.
"""

    response = llm.invoke(
        prompt
    )

    return response.content