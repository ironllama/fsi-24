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
    # all_drinks = filter(lambda drink: drink, all_drinks)  # Returns a filter object
#     new_drinks = []
#     for drink in all_drinks:
#         if drink:
#             new_drink = {}
#             for k, v in drink.items():
#                 if v:
#                    new_drink[k] = v
#             new_drinks.append(new_drink)
#     all_drinks = new_drinks
#     # all_drinks = list(all_drinks)

# with open("noNones.json", "w") as f:
#     json.dump(all_drinks, f, indent=2)

@app.get("/search")
def search():
    search_str = request.args.get("s")
    search_terms = search_str.split(",")

    all_matches = []
    for term in search_terms:
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

@app.get("/ingredients")
def ingredients():
    search_str = request.args.get("s")
    search_terms = search_str.split(",")

    all_matches = []
    for term in search_terms:
        for drink in all_drinks:
            for i in range(1, 16):
                curr_ingredient = drink["strIngredient" + str(i)]
                if curr_ingredient is not None:
                    if term.lower() in curr_ingredient.lower():
                        new_match = { "id": drink["idDrink"], "name": drink["strDrink"], "ingredient": curr_ingredient }
                        all_matches.append(new_match)
                else:
                    break  # breaks range loop
    
    return all_matches

@app.get("/details/<drink_id>")
def details(drink_id):
    for drink in all_drinks:
        if drink and drink["idDrink"] == drink_id:
            # return drink
            str_return = f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{drink["strDrink"]}</title>
    <style>
        body {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            font-family: sans-serif;
            font-size: 1.5rem;
        }}

        h1 {{
            font-size: 4rem;
            border-bottom: 1px solid grey;
        }}

        .imgWrapper {{
            border-radius: 5px;
            height: 15rem;
            width: 15rem;
            overflow: hidden;
            background-image: url("https://www.thecocktaildb.com/images/media/drink/rwsyyu1483388181.jpg");
            background-size: cover;
            background-position: center;
        }}
    </style>
</head>

<body>
    <h1>{drink["strDrink"]}</h1>
    <div style="width: 80%; display: flex; gap: 2rem;">
        <div class="imgWrapper"></div>
        <div>
            <ol>
"""
            for i in range(1, 16):
                if drink[f'strIngredient{i}']:
                    str_return += f"<li>{drink['strMeasure' + str(i)]} {drink['strIngredient' + str(i)]}</li>"
                
            str_return += f"""
            </ol>
            <p>
                {drink["strInstructions"]}
            </p>
        </div>
    </div>
</body>

</html>
"""
            return str_return
