from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def should_save_memory(text):

    prompt = f"""
You are a memory classifier.

Should this information be saved
for future conversations?

Save only if it contains:

- Name
- Profession
- Skills
- Preferences
- Goals
- Personal facts

Text:
{text}

Answer ONLY:

YES

or

NO
"""

    response = llm.invoke(prompt)

    answer = response.content.strip().upper()

    return "YES" in answer