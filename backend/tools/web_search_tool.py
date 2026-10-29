from ddgs import DDGS


def web_search(query: str, max_results: int = 5):

    try:
        results = DDGS().text(
            query,
            max_results=max_results
        )

        search_results = []

        for result in results:
            search_results.append({
                "title": result.get("title"),
                "url": result.get("href"),
                "snippet": result.get("body")
            })

        return {
            "success": True,
            "query": query,
            "results": search_results
        }

    except Exception as e:

        return {
            "success": False,
            "query": query,
            "results": [],
            "error": str(e)
        }