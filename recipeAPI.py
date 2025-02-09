import requests
api_url = "https://api.spoonacular.com/recipes/complexSearch"
api_key = "my_api_key"
params = { "query": "pizza", "apiKey": api_key}
response = requests.get(api_url, params=params)
data = response.json()
for recipe in data['results']:
    print(f"Title: {recipe['title']}")
    print(f"Image URL: {recipe['image']}")
    print("---")
