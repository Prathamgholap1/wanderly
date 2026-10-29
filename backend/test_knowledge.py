from agents.knowledge_agent import extract_stable_knowledge
from rag.knowledge_store import save_knowledge


research = """
Goa is a popular tourist destination in India.

Baga Beach is known for its beach activities
and nightlife.

Palolem Beach is known for its scenic coastline.

The temperature this weekend is expected to be 31°C.

Hotel XYZ currently costs ₹4,500 per night.

Goa has Portuguese-influenced architecture
and a rich cultural history.
"""


# Extract stable information
knowledge = extract_stable_knowledge(
    destination="Goa",
    research=research
)


print("\n========== EXTRACTED KNOWLEDGE ==========\n")

print(knowledge)


# Save to ChromaDB
saved = save_knowledge(
    destination="Goa",
    knowledge=knowledge
)


print("\n========== STORAGE ==========\n")

print(f"Saved {saved} knowledge chunks.")