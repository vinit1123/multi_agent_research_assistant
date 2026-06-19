from ddgs import DDGS

def web_search(query, max_results=5):

    results = []

    with DDGS() as ddgs:

        search_results = list(
            ddgs.text(
                query,
                max_results=max_results
            )
        )

        for r in search_results:

            results.append(
                {
                    "title": r.get("title", ""),
                    "body": r.get("body", ""),
                    "href": r.get("href", "")
                }
            )

    return results