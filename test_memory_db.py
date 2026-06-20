from memory_manager import (
    save_long_term_memory,
    search_memory
)

save_long_term_memory(
    "My name is Vinit"
)

save_long_term_memory(
    "I am a QA Lead"
)

save_long_term_memory(
    "I want to become a GenAI Developer"
)

print("\nMEMORY SEARCH:\n")

results = search_memory(
    "What do you know about me?"
)

for doc in results:

    print(doc.page_content)