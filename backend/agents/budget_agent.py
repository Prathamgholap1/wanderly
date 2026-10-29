from models.trip import TripRequest
from models.budget import BudgetBreakdown


def budget_agent(trip: TripRequest) -> BudgetBreakdown:

    # Temporary assumptions for our prototype
    fuel = 2000
    food_per_person_per_day = 500
    accommodation = 3000

    food = (
        food_per_person_per_day
        * trip.number_of_people
        * trip.duration_days
    )

    total = fuel + food + accommodation

    remaining = trip.budget - total

    return BudgetBreakdown(
        fuel=fuel,
        food=food,
        accommodation=accommodation,
        total=total,
        budget=trip.budget,
        remaining=remaining,
        within_budget=remaining >= 0
    )