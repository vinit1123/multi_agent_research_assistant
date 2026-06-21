from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

PERSONAL_PATTERNS = [
    "my name is",
    "i am",
    "i work as",
    "i work at",
    "i live in",
    "i want to",
    "my goal is",
    "i like",
    "i prefer",
    "my profession",
    "my job",
    "my age",
    "my experience"
]

def should_save_memory(text):

    text_lower = text.lower()

    # Fast rule-based check
    if any(
        pattern in text_lower
        for pattern in PERSONAL_PATTERNS
    ):
        return True

    # Skip obvious non-personal content
    if any(
        word in text_lower
        for word in [
            "news",
            "latest",
            "today",
            "weather",
            "stock",
            "price",
            "ai news"
        ]
    ):
        return False

    # LLM fallback
    prompt = f"""
You are a memory classifier.

Save ONLY long-term personal facts:

Examples:
- My name is Vinit
- I am a QA Lead
- I live in India
- I want to become a GenAI Developer
- I like cricket

Do NOT save:
- News
- Temporary questions
- Current events
- Search queries
- General knowledge questions

Text:
{text}

Answer ONLY:
YES
or
NO
"""

    response = llm.invoke(prompt)

    answer = response.content.strip().upper()

    return answer == "YES"