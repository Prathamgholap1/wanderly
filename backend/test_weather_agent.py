from agents.weather_agent import weather_agent


print("\n========== WEATHER AGENT TEST ==========\n")


result = weather_agent(
    "Manali, Himachal Pradesh, India"
)


print("SUCCESS:")
print(result["success"])

print("\nLOCATION:")
print(result["location"])

print("\nWEATHER DATA:")
print(result["weather_data"])

print("\nAI SUMMARY:")
print(result["summary"])