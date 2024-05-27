// This was a script to download the complete list of drinks. This was run with nodejs and is not something that I expect you to know, but I'm providing it, if you're curious!
const fs = require('fs');

all_drinks = JSON.parse(fs.readFileSync("cocktails.json", { encoding: "utf8" }))

fetch("https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list")
    .then(res => res.json())
    .then(res => {
        all_ingredients = res.drinks.map(i => i.strIngredient1)
        downloadByIngredients(all_ingredients);
    })

function downloadByIngredients(all_ingredients) {
    const fetchPromisesArray = all_ingredients.map(i => {
        return fetch("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=" + i)
            .then(res => res.json());
    });

    Promise.all(fetchPromisesArray)
        .then(allResults => {
            // allResults = allResults.drinks.flat();
            // allResults = allResults.reduce((acc, v) => v.drinks ? acc.concat(v.drinks) : acc, []);
            // require('fs').writeFileSync("allCocktails.json", JSON.stringify(allResults));
            allResults.drinks.forEach(drink => addDrink(drink));
        })
        .then(_ => all_drinks.sort((a, b) => a.strName < b.strName))
        .then(_ => fs.writeFileSync("new_cocktails.json", JSON.stringify(all_drinks)))
}

function addDrink(new_drink) {
    if (!all_drinks.some(drink => drink.strName === new_drink.strName))
        all_drinks.push(all_drinks);
}
