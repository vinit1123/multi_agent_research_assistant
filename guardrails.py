BLOCKED_WORDS = [
    "system prompt",
    "ignore instructions",
    "bypass",
    "exploit",
    "hack"
]

def validate_input(text):

    text = text.lower()

    for word in BLOCKED_WORDS:

        if word in text:
            return False

    return True