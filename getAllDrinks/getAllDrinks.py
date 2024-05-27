import requests
import json
import time

with open("cocktails.json", encoding="utf-8") as f:
    all_drinks = json.load(f)

all_drinks = [drink for drink in all_drinks if drink]  # Remove nulls

# First get all the ingredients
all_ingredients = requests.get(
    "https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list"
    ).json()
all_ingredients = all_ingredients["drinks"]

# For each ingredient, get matching drinks
for curr_ingredient in all_ingredients:
    print("INGRE:", curr_ingredient["strIngredient1"])
    new_drinks = requests.get(
        "https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=" + curr_ingredient["strIngredient1"]
        ).json()
    new_drinks = new_drinks["drinks"]

    # Matching drinks only have id, name, and pic. Need to get details
    for curr_drink in new_drinks:
        # First, check to see if it doesn't already exist in all_drinks
        if not any(drink for drink in all_drinks if drink["strDrink"] == curr_drink["strDrink"]):
            drink_detail = requests.get(
                "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=" + curr_drink["idDrink"]
                ).json()
            drink_detail = drink_detail["drinks"][0]
            if drink_detail:
                all_drinks.append(drink_detail)
    
    # The API is rate-limited. Let's slow things down
    time.sleep(0.1)

# Write to temp file, in case the sort crashes...
with open("unsorted_cocktails.json", "w") as f:
    json.dump(all_drinks, f)

all_drinks.sort(key=lambda d: d["strDrink"])

with open("new_cocktails.json", "w") as f:
    json.dump(all_drinks, f)
