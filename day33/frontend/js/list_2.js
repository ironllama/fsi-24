// SAME CODE FROM VERSION 1
// ============================================================================
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


// ADDED NEW CODE FOR VERSION 2
// ============================================================================
const formElem = document.querySelector("#listForm");
const newItemElem = document.querySelector("#newItem");

formElem.addEventListener("submit", evt => {
    evt.preventDefault();

    sendItemToBack(newItemElem.value);
    newItemElem.value = "";
});

function sendItemToBack(item) {
    // Send item to backend.
    fetch(api_server + "/newItem", {
        method: "post",
        body: item
    })
        .then(res => res.text())
        .then(res => {
            if (res == 'OK') {
                addItemToList(item);
            }
        });
}