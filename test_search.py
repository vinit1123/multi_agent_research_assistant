from ddgs import DDGS

print("Starting search...")

with DDGS() as ddgs:
    print("Connected")

    results = list(
        ddgs.text(
            "Latest AI news",
            max_results=3
        )
    )

print("Results received")
print(results)