from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def supervisor(question: str):

    prompt = f"""
You are a routing agent.

Choose ONLY ONE route:

tool
research
summary
writer
chat

Rules:

tool:
- Math calculations
- Arithmetic expressions
- Memory lookup
- Personal information lookup
- "What do you know about me"
- "Who am I"
- User profile questions

research:
- Current events
- News
- AI topics
- Technologies
- Factual questions
- Research questions

summary:
- Summarize text
- Create summary
- Shorten content

writer:
- Write article
- Write blog
- Write report
- Generate document

chat:
- Greetings
- Casual conversation
- General chat

Question:
{question}

Return ONLY one word:
tool
research
summary
writer
chat
"""

    response = llm.invoke(prompt)

    route = response.content.strip().lower()

    print("\nRAW ROUTE:", route)

    if "tool" in route:
        return "tool"

    elif "research" in route:
        return "research"

    elif "summary" in route:
        return "summary"

    elif "writer" in route:
        return "writer"

    else:
        return "chat"