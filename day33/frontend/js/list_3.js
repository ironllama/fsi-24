// Get list of items from backend
// ============================================================================
const api_server = "http://localhost:5000";

const listItemsElem = document.querySelector("#listItems");

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
// showListOfItems("2|apples,12|oranges,34|lemons,14|kiwi,1|watermelon");

function addItemToList(item) {
    // const [amt, item] = item.split("|");
    // const newItem = amt + " " + item;
    item = item.replace("|", "x ");

    const newElem = document.createElement("li");
    newElem.className = "listItem";
    newElem.textContent = item;

    listItemsElem.appendChild(newElem);
}


// Send new item to backend
// ============================================================================
const newItemElem = document.querySelector("#newItem");
const newAmtElem = document.querySelector("#newAmt");

newItemElem.addEventListener("keyup", evt => {
    if (evt.key == "Enter") {
        sendItemToBack(newAmtElem.value + "|" + newItemElem.value);
        newAmtElem.value = "";
        newItemElem.value = "";
    }
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