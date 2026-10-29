from agents.orchestrator import wanderly_orchestrator


query = """
I want to visit Lonavala for 2 days with 7 friends.

We are starting from Mumbai and travelling by car.

Our total budget is ₹8000.

We love nature, viewpoints and photography.
"""


result = wanderly_orchestrator(query)


trip = result["trip"]
budget = result["budget"]
itinerary = result["itinerary"]


print("\n========== WANDERLY ==========\n")

print("Destination:", trip.destination)
print("Duration:", trip.duration_days, "days")
print("People:", trip.number_of_people)
print("Budget:", f"₹{trip.budget}")
print("Starting Location:", trip.starting_location)
print("Transport:", trip.transport)
print("Interests:", trip.interests)


print("\n========== BUDGET ==========\n")

print("Fuel:", f"₹{budget.fuel}")
print("Food:", f"₹{budget.food}")
print("Accommodation:", f"₹{budget.accommodation}")
print("Total:", f"₹{budget.total}")
print("Remaining:", f"₹{budget.remaining}")
print("Within Budget:", budget.within_budget)


print("\n========== ITINERARY ==========\n")

print(itinerary)