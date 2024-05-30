// Get list of items from backend
// ============================================================================
const api_server = "http://localhost:5000";

const listItemsElem = document.querySelector("#listItems");

function getItemsFromBack() {
    // Get items and populate the list
    fetch(api_server + "/getItems")
        .then(res => res.json())
        .then(showListOfItems);
}
getItemsFromBack();

function showListOfItems(list) {
    if (list) {
        for (const item of list) {
            addItemToList(item);
        }
    }
}
// Just for testing.
// showListOfItems("2|apples,12|oranges,34|lemons,14|kiwi,1|watermelon");

function addItemToList(item) {
    itemStr = item.amt + "x " + item.item;

    const newElem = document.createElement("li");
    newElem.className = "listItem";
    newElem.textContent = itemStr;

    listItemsElem.appendChild(newElem);
}


// Send new item to backend
// ============================================================================
const newItemElem = document.querySelector("#newItem");
const newAmtElem = document.querySelector("#newAmt");

newItemElem.addEventListener("keyup", evt => {
    if (evt.key == "Enter") {
        sendItemToBack({
            amt: newAmtElem.value,
            item: newItemElem.value
        });
        newAmtElem.value = "";
        newItemElem.value = "";
    }
});

function sendItemToBack(item) {
    // Send item to backend.
    fetch(api_server + "/newItem", {
        method: "post",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(item)
    })
        .then(res => res.json())
        .then(res => {
            if (res.message == 'OK') {
                addItemToList(item);
            }
        });
}