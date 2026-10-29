import os


from dotenv import load_dotenv
from google import genai

from rag.retriever import search_knowledge
from models.trip import TripRequest


# Load environment variables
load_dotenv()


# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_trip_request(user_query: str) -> TripRequest:

    prompt = f"""
Extract the travel requirements from the user's message.

If a value is not mentioned, return null.

Important:
- Budget must be represented as a number in Indian rupees.
- Do not include currency symbols.
- Example: ₹8,000 should become 8000.
- duration_days must be an integer.
- number_of_people must be an integer.
- interests must be a list of strings.

USER MESSAGE:

{user_query}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": TripRequest,
        },
    )

    return TripRequest.model_validate_json(response.text)


def travel_agent(user_query: str):

    # --------------------------------
    # STEP 1: Understand the user
    # --------------------------------

    trip = extract_trip_request(user_query)

    print("\n========== TRIP REQUIREMENTS ==========\n")
    print(trip)

    # --------------------------------
    # STEP 2: Search our RAG database
    # --------------------------------

    knowledge = search_knowledge(
        user_query,
        number_of_results=3
    )

    context = "\n\n".join(knowledge)

    # --------------------------------
    # STEP 3: Generate travel response
    # --------------------------------

    prompt = f"""
You are Wanderly, an intelligent travel planning assistant.

Create a practical travel recommendation based on the user's requirements.

TRIP REQUIREMENTS:

Destination:
{trip.destination}

Duration:
{trip.duration_days} days

Budget:
₹{trip.budget}

People:
{trip.number_of_people}

Starting Location:
{trip.starting_location}

Interests:
{trip.interests}

Transport:
{trip.transport}


RETRIEVED TRAVEL KNOWLEDGE:

{context}


RULES:

1. Use the retrieved knowledge as your primary source.
2. Do not invent specific facts.
3. If information is missing, clearly mention it.
4. Focus on the user's interests.
5. Keep the response practical.
6. Organize the response clearly.
"""

    # Ask Gemini to create the final travel response
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text

