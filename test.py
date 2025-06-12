from yelp_api import search_restaurants

results = search_restaurants("Los Angeles", food_type="tacos", price_level="1,2")

for place in results:
    print(f"{place['name']} - {place['rating']}⭐")
    print(place['location']['address1'], "\n")
