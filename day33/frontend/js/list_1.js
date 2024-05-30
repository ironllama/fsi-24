const listItemsElem = document.querySelector("#listItems");

const api_server = "http://localhost:5000";

function getItemsFromBack() {
    // Get items and populate the list
    fetch(api_server + "/getItems")
        .then(res => res.text())
        .then(res => showListOfItems(res));
}
getItemsFromBack();

function showListOfItems(list) {
    if (list) {
        const allItems = list.split(",").map(i => i.trim());
        for (const item of allItems) {
            addItemToList(item);
        }
    }
}
// Just for testing.
// showListOfItems("apples, oranges, lemons, kiwi, watermelon");

function addItemToList(item) {
    const newElem = document.createElement("li");
    newElem.className = "listItem";
    newElem.textContent = item;

    listItemsElem.appendChild(newElem);
}