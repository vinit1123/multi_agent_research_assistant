from memory_manager import (
    save_long_term_memory,
    search_memory
)

save_long_term_memory(
    "I live in India"
)

print("\nMEMORY SEARCH\n")

results = search_memory(
    "Where do I live?"
)

for doc in results:

    print(
        doc.page_content
    )