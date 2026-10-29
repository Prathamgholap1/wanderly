import requests


def get_coordinates(location: str):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": location,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(
        url,
        params=params,
        timeout=15
    )

    if response.status_code != 200:
        return {
            "success": False,
            "error": f"Geocoding service returned HTTP {response.status_code}"
        }

    data = response.json()

    if "results" not in data or not data["results"]:
        return {
            "success": False,
            "error": f"Could not find location: {location}"
        }

    result = data["results"][0]

    return {
        "success": True,
        "name": result["name"],
        "country": result.get("country"),
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }