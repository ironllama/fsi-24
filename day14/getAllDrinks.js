let allLetters = "abcdefghijklmnopqrstuvwxyz";

let allResults = Promise.all(
    allLetters.split("").map(letter => {
        return fetch("https://www.thecocktaildb.com/api/json/v1/1/search.php?f=" + letter)
            .then(res => res.json())
            .catch(err => console.log("ERRORS:", err))
    })
)

allResults.then(res => {
    const allDrinks = res.map(r => r.drinks).flat();
    require('fs').writeFileSync("cocktails.db", JSON.stringify(allDrinks));
});
