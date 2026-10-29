import chromadb
from rag.embeddings import generate_embedding


client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    name="wanderly_knowledge"
)


def search_knowledge(
    query: str,
    number_of_results: int = 3,
    category: str | None = None,
    destination: str | None = None
):

    query_embedding = generate_embedding(query)

    search_parameters = {
        "query_embeddings": [query_embedding],
        "n_results": number_of_results
    }

    filters = []

    if category:
        filters.append({
            "category": category
        })

    if destination:
        filters.append({
            "destination": destination.lower()
        })

    if len(filters) == 1:

        search_parameters["where"] = filters[0]

    elif len(filters) > 1:

        search_parameters["where"] = {
            "$and": filters
        }

    results = collection.query(
        **search_parameters
    )

    documents = results["documents"][0]
    distances = results["distances"][0]

    return {
        "documents": documents,
        "distances": distances
    }