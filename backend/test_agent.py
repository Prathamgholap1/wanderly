from agents.travel_agent import extract_trip_request
from agents.budget_agent import budget_agent


query = """
I want to visit Lonavala for 2 days with 5 friends.

We are starting from Mumbai and travelling by car.

Our total budget is ₹8000.

We love nature, viewpoints and photography.
"""


# --------------------------------
# STEP 1: Extract trip requirements
# --------------------------------

trip = extract_trip_request(query)

print("\n========== TRIP REQUIREMENTS ==========\n")
print(trip)


# --------------------------------
# STEP 2: Calculate budget
# --------------------------------

budget = budget_agent(trip)

print("\n========== BUDGET ==========\n")

print(f"Fuel: ₹{budget.fuel}")
print(f"Food: ₹{budget.food}")
print(f"Accommodation: ₹{budget.accommodation}")
print(f"Total: ₹{budget.total}")
print(f"Budget: ₹{budget.budget}")
print(f"Remaining: ₹{budget.remaining}")
print(f"Within Budget: {budget.within_budget}")