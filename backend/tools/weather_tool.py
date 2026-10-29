import requests

from tools.geocoding_tool import get_coordinates


def get_weather(location: str):

    # -----------------------------
    # STEP 1: Get coordinates
    # -----------------------------

    coordinates = get_coordinates(location)

    if not coordinates["success"]:
        return coordinates

    latitude = coordinates["latitude"]
    longitude = coordinates["longitude"]

    # -----------------------------
    # STEP 2: Get weather
    # -----------------------------

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code",
        "daily": (
            "temperature_2m_max,"
            "temperature_2m_min,"
            "precipitation_probability_max"
        ),
        "timezone": "auto"
    }

    response = requests.get(
        url,
        params=params,
        timeout=15
    )

    if response.status_code != 200:
        return {
            "success": False,
            "error": f"Weather service returned HTTP {response.status_code}"
        }

    data = response.json()

    # -----------------------------
    # STEP 3: Return useful data
    # -----------------------------

    return {
        "success": True,
        "location": coordinates["name"],
        "country": coordinates["country"],
        "latitude": latitude,
        "longitude": longitude,
        "current_temperature": data["current"]["temperature_2m"],
        "weather_code": data["current"]["weather_code"],
        "today_max_temperature": data["daily"]["temperature_2m_max"][0],
        "today_min_temperature": data["daily"]["temperature_2m_min"][0],
        "rain_probability": data["daily"]["precipitation_probability_max"][0]
    }