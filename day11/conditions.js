let word = "banana";

// let wordtest = (word === "banana");  // Right side evaluates NOW, for the assignment.
let wordtest = () => word === "banana";

word = "apple";

// console.log(wordtest);
// if (word === "banana") {
// if (wordtest) {  // wordtest has already been set to true
if (wordtest()) {  // wordtest has already been set to true
    console.log("It's a banana!");
}
else {
    console.log("It's NOT a banana!");
}

