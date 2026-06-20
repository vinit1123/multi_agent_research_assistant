from graph import workflow

result = workflow.invoke(
    {
        "question":
        "Latest AI news"
    }
)

print(
    result["report"]
)