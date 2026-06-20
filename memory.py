memory = []

def save_memory(role, content):

    memory.append(
        {
            "role": role,
            "content": content
        }
    )

def get_memory():

    print("\nMEMORY:")
    print(memory)

    return memory[-5:]

FOLLOWUP_WORDS = [
    "explain more",
    "tell me more",
    "more",
    "continue",
    "elaborate",
    "details"
]

def is_followup(question):

    q = question.lower()

    return any(
        word in q
        for word in FOLLOWUP_WORDS
    )
    memory = []

def save_memory(role, content):

    memory.append(
        {
            "role": role,
            "content": content
        }
    )

    if len(memory) > 10:
        memory.pop(0)
def get_formatted_memory():

    history = []

    for item in memory:

        history.append(
            f"{item['role'].upper()}: {item['content']}"
        )

    return "\n".join(history[-5:])