async function doThatThing() {
    let one = await fetch("https://ddragon.leagueoflegends.com/cdn/14.8.1/data/en_US/champion.json")
    let two = await one.json();
    const newNames = Object.values(two.data)  // Pull out values from jsonObj as an array.
        .map(c => c.name)  // Pull out only the names from each object
        .slice(0, 10)
        .join("|")

    // stuffElem[1].innerHTML = newNames;
    // console.log("NAMES:", newNames);
    return newNames;
}
// doThatThing();

async function middleOfCode() {
    const backFromThing = await doThatThing();
    // console.log("BACK:", backFromThing);
    // const one = backFromThing.then(function (res) {
    //     return res
    // });
    // one.then(what => console.log("WHAT:", what));
    console.log("FINISHED WITH middleOfCode()");
    return backFromThing;
}

// const three = middleOfCode();
// three.then(stuff => {
//     console.log("FINISHED:", stuff);
// });
async function four() {
    const three = await middleOfCode();
    console.log("FINISHED:", three);
}
// const five = four();
// console.log("FIVE:", five);
four();

function six() {
    console.log("SIX");
}
six();

console.log("FIRST OR LAST?");
