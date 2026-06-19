from langchain_ollama import ChatOllama

print("Creating model...")

llm = ChatOllama(
    model="llama3.2",
    base_url="http://127.0.0.1:11434"
)

print("Calling model...")

response = llm.invoke("hi")

print("DONE")

print(response.content)