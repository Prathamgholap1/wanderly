from tools.geocoding_tool import get_coordinates


print("\n========== GEOCODING TEST ==========\n")


result = get_coordinates(
    "Manali, Himachal Pradesh, India"
)


print(result)