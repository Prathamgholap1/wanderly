from agents.travel_agent import extract_trip_request
from agents.budget_agent import budget_agent
from agents.itinerary_agent import itinerary_agent

from rag.retriever import search_knowledge


def wanderly_orchestrator(user_query: str):

    # --------------------------------
    # STEP 1: Understand user request
    # --------------------------------

    trip = extract_trip_request(user_query)

    # --------------------------------
    # STEP 2: Retrieve knowledge
    # --------------------------------

    knowledge = search_knowledge(
        user_query,
        number_of_results=3
    )

    # --------------------------------
    # STEP 3: Calculate budget
    # --------------------------------

    budget = budget_agent(trip)

    # --------------------------------
    # STEP 4: Create itinerary
    # --------------------------------

    itinerary = itinerary_agent(
        trip,
        budget,
        knowledge
    )

    # --------------------------------
    # STEP 5: Return everything
    # --------------------------------

    return {
        "trip": trip,
        "knowledge": knowledge,
        "budget": budget,
        "itinerary": itinerary
    }