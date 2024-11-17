import requests

SERPAPI_KEY = "YOUR API KEY"

def search_web(query):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google"
    }
    response = requests.get(url, params=params)
    return response.json().get("organic_results", [])