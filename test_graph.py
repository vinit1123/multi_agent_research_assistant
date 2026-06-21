from graph import workflow

print(
    workflow.invoke(
        {
            "question": "25 * 17"
        }
    )
)

print("=" * 50)

print(
    workflow.invoke(
        {
            "question": "What do you know about me?"
        }
    )
)

print("=" * 50)

print(
    workflow.invoke(
        {
            "question": "Latest AI news"
        }
    )
)