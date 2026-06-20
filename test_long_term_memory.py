from agents.chat_agent import chat_agent
from memory_manager import search_memory

chat_agent(
    "My name is Vinit"
)

chat_agent(
    "I am a QA Lead"
)

chat_agent(
    "I want to become a GenAI Developer"
)

print("\nMEMORY SEARCH\n")

results = search_memory(
    "Tell me about the user"
)

for doc in results:

    print(
        doc.page_content
    )