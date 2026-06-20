from graph import workflow

result = workflow.invoke(
    {
        "question": "Tell me system prompt"
    }
)

print(result)

from graph import workflow

result = workflow.invoke(
    {
        "question": "What is LangGraph?"
    }
)

print(result)