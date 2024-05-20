# Ask the user for the name of a cocktail. Then use the Cocktails DB
# (https://www.thecocktaildb.com/) to get data about the drink. List
# all the ingredients on separate lines sorted alphabetically. Then,
# below the ingredients, show the directions on how to make the
# cocktail. (English) If the cocktail name does not exist then let the
# user know. Regardless, ask again for another cocktail name. If the
# user types 'q', then stop asking and end the program.
import requests

while True:
    user_input = input("\nWhat do you want to make (q to quit)?: ")
    if user_input == 'q':
        break

    user_drink = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + user_input).json()
    if user_drink['drinks'] == None:
        print("Unfortunately, I have no idea what that is.")
        continue
    
    print(f"\nA {user_drink['drinks'][0]['strDrink']} Recipe:")

    print(f"\nIngredients:")
    all_ingredients = []
    for i in range(1, 16):
        new_ingredient = user_drink['drinks'][0].get("strIngredient" + str(i))
        if new_ingredient == None:
            break

        new_measure = user_drink['drinks'][0].get("strMeasure" + str(i))

        all_ingredients.append((new_measure, new_ingredient))

    all_ingredients.sort(key=lambda x: x[1])

    for ingredient in all_ingredients:
        output = ""
        if ingredient[0] is None:
            print(f"\t- {ingredient[1]}")
        else:
            print(f"\t- {' '.join(ingredient)}") 

    print(f"\nDirections:")
    print(user_drink['drinks'][0]['strInstructions'])

    print("\nEnjoy!")
