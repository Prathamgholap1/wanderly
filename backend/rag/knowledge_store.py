import chromadb

from rag.embeddings import generate_embedding


client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="wanderly_knowledge"
)


def save_knowledge(
    destination: str,
    knowledge: str,
    category: str = "research"
):

    chunks = [
        chunk.strip()
        for chunk in knowledge.split("\n")
        if chunk.strip()
    ]

    saved = 0

    for index, chunk in enumerate(chunks):

        embedding = generate_embedding(chunk)

        document_id = (
            f"research_"
            f"{destination.lower()}_"
            f"{index}"
        )

        collection.upsert(
            ids=[document_id],
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[{
                "source": "web_research",
                "category": category,
                "destination": destination.lower()
            }]
        )

        saved += 1

    return saved