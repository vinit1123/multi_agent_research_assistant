import ollama

print("Calling Ollama directly...")

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "What is Artificial Intelligence?"
        }
    ]
)

print("DONE")
print(response["message"]["content"])