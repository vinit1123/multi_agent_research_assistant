from agents.summarizer_agent import summarizer_agent

text = """
Artificial Intelligence is rapidly
transforming industries.

Companies are investing heavily
in AI research and development.

New AI models are improving
reasoning, coding and search.
"""

result = summarizer_agent(text)

print(result)