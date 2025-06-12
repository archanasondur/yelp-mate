import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("YELP_API_KEY")

YELP_SEARCH_URL = "https://api.yelp.com/v3/businesses/search"

def search_restaurants(location, food_type="restaurant", price=None, max_results=5):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    params = {
        "location": location,
        "term": food_type,
        "limit": max_results,
        "sort_by": "rating",  
    }

    if price:
        params["price"] = price
  

    response = requests.get(YELP_SEARCH_URL, headers=headers, params=params)

    if response.status_code != 200:
        print("Something went wrong:", response.status_code, response.text)
        return []

    data = response.json()
    return data.get("businesses", [])
