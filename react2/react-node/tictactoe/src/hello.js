for (let i = 0; i < 10; i++) console.log("HEEEEELLLLOOOOO!");

const googleText = await fetch("https://www.google.com");
const googleHTML = await googleText.text();
console.log(googleHTML);
