from agents.research_agent import research_destination


print("\n========================================")
print("       WANDERLY RESEARCH AGENT")
print("========================================")


print("\n\nTEST — GOA")
print("----------------------------------------")

result = research_destination(
    destination="Goa",
    question="What are good places for photography?"
)

print("\nSOURCE:")
print(result["source"])

print("\nANSWER:")
print(result["answer"])

print("\nNEEDS WEB:")
print(result["needs_web"])


print("\n\nTEST — GOA WEATHER")
print("----------------------------------------")

result = research_destination(
    destination="Goa",
    question="What is the weather forecast for this weekend?"
)

print("\nSOURCE:")
print(result["source"])

print("\nANSWER:")
print(result["answer"])

print("\nNEEDS WEB:")
print(result["needs_web"])