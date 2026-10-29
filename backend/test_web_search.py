from tools.web_search_tool import web_search


print("\n========== WEB SEARCH TEST ==========\n")


result = web_search(
    "best places to visit in Manali Himachal Pradesh"
)


print("SUCCESS:")
print(result["success"])

print("\nQUERY:")
print(result["query"])

print("\nRESULTS:\n")


for item in result["results"]:

    print("TITLE:")
    print(item["title"])

    print("\nURL:")
    print(item["url"])

    print("\nSNIPPET:")
    print(item["snippet"])

    print("\n-----------------------------\n")