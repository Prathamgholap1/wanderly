from rag.retriever import search_knowledge


print("\n========== GENERAL SEARCH ==========\n")

results = search_knowledge(
    "What can I do in Lonavala?",
    number_of_results=3
)

for result in results:
    print(result)
    print("\n---\n")


print("\n========== SAFETY SEARCH ==========\n")

results = search_knowledge(
    "What should I be careful about during monsoon?",
    number_of_results=3,
    category="safety"
)

for result in results:
    print(result)
    print("\n---\n")\


print("\n========== LONAVALA DESTINATION SEARCH ==========\n")

results = search_knowledge(
    "What are good places for photography?",
    number_of_results=3,
    destination="lonavala"
)

for result in results:
    print(result)
    print("\n---\n")