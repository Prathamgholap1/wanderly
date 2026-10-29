import os

from dotenv import load_dotenv
from google import genai

from tools.weather_tool import get_weather


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


MODEL = "gemini-3.5-flash-lite"


def weather_agent(location: str):

    # Get real weather data
    weather = get_weather(location)

    # If weather API failed
    if not weather["success"]:
        return {
            "success": False,
            "error": weather["error"]
        }

    # Give the weather data to Gemini
    prompt = f"""
You are Wanderly's Weather Agent.

Give the user a simple and useful weather summary.

Weather data:

Location: {weather["location"]}
Country: {weather["country"]}
Current temperature: {weather["current_temperature"]}°C
Today's maximum: {weather["today_max_temperature"]}°C
Today's minimum: {weather["today_min_temperature"]}°C
Rain probability: {weather["rain_probability"]}%

Instructions:
- Explain the weather in simple language.
- Mention the temperature.
- Mention rain probability.
- Give a short travel suggestion based on the weather.
- Do not invent weather information.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return {
        "success": True,
        "location": weather["location"],
        "weather_data": weather,
        "summary": response.text
    }