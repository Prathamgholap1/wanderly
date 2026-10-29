import chromadb
from pathlib import Path

from rag.embeddings import generate_embedding


DATA_PATH = Path("data")

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="wanderly_knowledge"
)


def chunk_text(text: str, chunk_size: int = 500):

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):

        chunk = " ".join(
            words[i:i + chunk_size]
        )

        chunks.append(chunk)

    return chunks


def load_documents():

    documents = []

    for file in DATA_PATH.rglob("*.md"):

        text = file.read_text(
            encoding="utf-8"
        )

        chunks = chunk_text(text)

        # Get destination name
        destination = file.stem.split("_")[0].lower()

        for index, chunk in enumerate(chunks):

            documents.append({
                "id": f"{file.stem}_{index}",
                "text": chunk,
                "source": file.name,
                "category": file.parent.name,
                "destination": destination
            })

    return documents


def ingest_documents():

    documents = load_documents()

    for document in documents:

        # Generate local embedding
        embedding = generate_embedding(
            document["text"]
        )

        collection.upsert(
            ids=[document["id"]],
            documents=[document["text"]],
            embeddings=[embedding],
            metadatas=[{
                "source": document["source"],
                "category": document["category"],
                "destination": document["destination"]
            }]
        )

    print(
        f"Inserted {len(documents)} chunks."
    )


if __name__ == "__main__":
    ingest_documents()