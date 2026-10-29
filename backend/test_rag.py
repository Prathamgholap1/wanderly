from rag.retriever import search_knowledge


query = "What are the best nature places to visit in Lonavala?"

results = search_knowledge(query)

print("\n--- Retrieved Knowledge ---\n")

for result in results:
    print(result)