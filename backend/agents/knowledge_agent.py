import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-3.5-flash-lite"


def extract_stable_knowledge(destination: str, research: str):

    prompt = f"""
You are Wanderly's Knowledge Processing Agent.

Destination:
{destination}

Web research:
{research}

Your job is to extract ONLY stable travel knowledge
that would remain useful for months or years.

KEEP:
- Tourist attractions
- Places to visit
- Activities
- General destination information
- History and culture
- General safety information
- General travel tips

DO NOT KEEP:
- Weather forecasts
- Current temperature
- Hotel prices
- Restaurant prices
- Current availability
- Traffic conditions
- Temporary events
- Today's opening status
- Any information that changes frequently

Return only the useful stable knowledge as
clear factual bullet points.

Do not add information that is not present
in the research.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text