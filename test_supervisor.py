from agents.supervisor import supervisor

question = input("Question: ")

route = supervisor(question)

print("Route:", route)