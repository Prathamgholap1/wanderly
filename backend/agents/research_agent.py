from google import genai
import os
from dotenv import load_dotenv

from rag.retriever import search_knowledge
from tools.web_search_tool import web_search

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-3.5-flash-lite"


def research_destination(destination: str, question: str):

    rag_result = search_knowledge(
        question,
        number_of_results=3,
        destination=destination
    )

    knowledge = rag_result["documents"]
    distances = rag_result["distances"]

    # --------------------------------
    # CHECK RAG RELEVANCE
    # --------------------------------

    if knowledge:

        best_distance = distances[0]

        # Lower distance = better match
        RAG_THRESHOLD = 1.55

        if best_distance <= RAG_THRESHOLD:

            context = "\n\n".join(knowledge)

            prompt = f"""
You are Wanderly's Research Agent.

Destination:
{destination}

User Question:
{question}

Wanderly Knowledge:
{context}

Answer the user's question using the
provided Wanderly knowledge.

Rules:
- Do not invent facts.
- Only use the provided knowledge.
- Keep the answer useful and concise.
"""

            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )

            return {
                "success": True,
                "source": "rag",
                "answer": response.text,
                "needs_web": False
            }

    # --------------------------------
    # RAG NOT RELEVANT
    # --------------------------------

    search_query = f"{question} {destination}"

    search_result = web_search(
        search_query,
        max_results=5
    )

    if not search_result["success"]:
        return {
            "success": False,
            "source": "web",
            "answer": None,
            "needs_web": True,
            "error": search_result["error"]
        }

    search_context = ""

    for result in search_result["results"]:

        search_context += f"""
Title: {result["title"]}
URL: {result["url"]}
Information: {result["snippet"]}

"""

    prompt = f"""
You are Wanderly's Research Agent.

Destination:
{destination}

User Question:
{question}

The following information was retrieved
from web search:

{search_context}

Answer the user's question using the
information found in the search results.

Rules:
- Do not invent information.
- Prefer reliable sources.
- Clearly explain the useful findings.
- Keep the answer concise.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return {
        "success": True,
        "source": "web",
        "answer": response.text,
        "needs_web": True,
        "search_results": search_result["results"]
    }