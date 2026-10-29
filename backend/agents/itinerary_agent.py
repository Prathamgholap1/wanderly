import os

from dotenv import load_dotenv
from google import genai

from models.trip import TripRequest
from models.budget import BudgetBreakdown


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def itinerary_agent(
    trip: TripRequest,
    budget: BudgetBreakdown,
    knowledge: list[str]
):

    context = "\n\n".join(knowledge)

    prompt = f"""
You are Wanderly's Itinerary Agent.

Create a practical day-by-day travel itinerary.

USER REQUIREMENTS
-----------------

Destination:
{trip.destination}

Duration:
{trip.duration_days} days

Number of Travelers:
{trip.number_of_people}

Starting Location:
{trip.starting_location}

Transport:
{trip.transport}

Interests:
{trip.interests}

Maximum Budget:
₹{trip.budget}


BUDGET ANALYSIS
---------------

Fuel:
₹{budget.fuel}

Food:
₹{budget.food}

Accommodation:
₹{budget.accommodation}

Estimated Total:
₹{budget.total}

Remaining Budget:
₹{budget.remaining}

Within Budget:
{budget.within_budget}


TRAVEL KNOWLEDGE
----------------

{context}


INSTRUCTIONS
------------

1. Create a day-by-day itinerary.
2. Prioritize activities matching the user's interests.
3. Use places from the provided travel knowledge.
4. Do not invent specific facts about places.
5. If the estimated trip exceeds the budget, mention it.
6. Suggest ways to reduce costs where possible.
7. Include safety considerations when relevant.
8. Keep the itinerary practical.
9. Do not claim exact prices unless they are provided.
10. Clearly separate known information from suggestions.


FORMAT
------

# Wanderly Trip Plan

## Trip Overview

Destination:
Duration:
Travelers:
Transport:
Budget:

## Day 1

Morning:
...

Afternoon:
...

Evening:
...

## Day 2

Morning:
...

Afternoon:
...

Evening:
...

## Budget Status

Estimated Cost:
User Budget:
Difference:

## Important Tips

- ...
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text