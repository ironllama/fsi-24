"""
    Create an API server for drink data. Use the 'cocktails.json' file as the source of data for your server. Your server should have the following endpoints and behaviors:

    /search
        This API endpoint accepts a query parameter 's', that allows the user to search all drinks for drink names that match the word(s) provided in 's'. Multiple search terms can be provided as a comma separated list of terms and the search should match on names including any of those terms. This returns an array of matching drink names and respective ids.
    /ingredients
        This API endpoint accepts a query parameter 's', that allows the user to search all drinks for drink ingredients that match the word(s) provided in 's'. Multiple search terms can be provided as a comma separated list of terms and the search should match on ingredients including any of those terms. This returns an array of matching drink names and respective ids.
    /details/<drink_id>
        This API endpoint uses the path
          parameter to find a specific drink and returns all the details of that drink.

    Then create a UI that uses the API server above to give the user the ability to search by drink name or particular ingredients. (Two different forms, please.) Once the user receives a list of matches from either one of the searches, clicking on one of the matches will provide all the details of that drink on another page in an attractive way.
"""
from flask import Flask, request
import json

app = Flask(__name__)

with open("cocktails.json", encoding="utf-8") as drink_file:
    all_drinks = json.load(drink_file)  # Parse the JSON file. Original JSON parent structure is a list.
    # all_names = [(drink["idDrink"], drink["strDrink"]) for drink in all_drinks]
    all_drinks = filter(lambda drink: drink is not None, all_drinks)  # Returns a filter object
    all_drinks = list(all_drinks)

@app.get("/search")
def search():
    search_terms = request.args.get("s")

    all_matches = []
    search_list = search_terms.split(",")
    for term in search_list:
        # all_matches += [
        #     (drink["idDrink"], drink["strDrink"]) \
        #     for drink in all_drinks \
        #     if "strDrink" in drink and term.lower() in drink["strDrink"].lower()
        # ]
        # Same as comprehension above, since it's a bit incomprehensible
        for drink in all_drinks:
            if "strDrink" in drink and term.lower() in drink["strDrink"].lower():
                new_match = { "id": drink["idDrink"], "name": drink["strDrink"] }
                all_matches.append(new_match)
    
    return all_matches