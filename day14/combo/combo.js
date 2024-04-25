function createCombo(rootElemId, allItems, nameKey, getInfoLayout) {
    const rootElem = document.querySelector("#" + rootElemId);

    rootElem.innerHTML = `
        <div class="comboWrapper">
            <div class="inputArea">
                <input id="userInput" autofocus>
                <button>Go</button>
                <div class="matches"></div>
            </div>
            <div class="info"></div>
        </div>
    `;


    // Get the variables to the stuff in the DOM tree.
    const inputElem = document.querySelector(`#${rootElemId} input`);
    const matchesElem = document.querySelector(`#${rootElemId} .matches`);
    const buttonElem = document.querySelector(`#${rootElemId} button`);
    const infoElem = document.querySelector(`#${rootElemId} .info`);

    function setInputValue(itemName) {
        inputElem.value = itemName;  // Make input match what we clicked on.
        inputElem.focus();

        // Blank out the matches, once we've clicked on an item in the list.
        matchesElem.replaceChildren();
        matchesElem.style.display = "none";
    }

    function submitItem() {
        // Find the item that matches what we typed into the input.
        const matchingItem =
            allItems
                .find(item => item[nameKey].toLowerCase() === inputElem.value.toLowerCase())

        // Since Array.prototype.find returns an undefined if it doesn't find a match, we test for it.
        if (matchingItem !== undefined) {  // If we found a match...

            matchesElem.replaceChildren();
            matchesElem.style.display = "none";

            // Fill in the matchingItem inside the info area.
            const newHtml = getInfoLayout(matchingItem);

            infoElem.innerHTML = newHtml;
        }
    }

    inputElem.addEventListener("input", () => {
        if (inputElem.value.length > 2) {
            matchesElem.replaceChildren();  // Clear out old matches.

            // Add new matches.
            matchesElem.style.display = "block";
            allItems
                .filter(item => item[nameKey].toLowerCase().includes(inputElem.value.toLowerCase()))
                .forEach((item, i) => {
                    // Create new item to add to matches list.
                    const newItem = document.createElement("a");
                    // newItem.href="#";
                    newItem.tabIndex = i;  // For the focus to work properly.
                    newItem.innerHTML = item[nameKey];
                    matchesElem.appendChild(newItem);

                    newItem.addEventListener("click", () => {
                        setInputValue(item[nameKey]);  // Make input match what we clicked on.
                    });

                    newItem.addEventListener("keydown", (evt) => {
                        if (i > 0 && evt.key === "ArrowUp") {
                            matchesElem.children[i - 1].focus();
                            inputElem.value = matchesElem.children[i - 1].innerHTML;
                        }
                        else if (i < matchesElem.children.length - 1 && evt.key === "ArrowDown") {
                            matchesElem.children[i + 1].focus();
                            inputElem.value = matchesElem.children[i + 1].innerHTML;
                        }
                    });

                    newItem.addEventListener("keyup", (evt) => {
                        if (evt.key === "Enter") {
                            setInputValue(item[nameKey]);
                        }
                    });
                });
        }
    });

    inputElem.addEventListener("keyup", (evt) => {
        if (matchesElem.style.display !== "none" && evt.key === "ArrowDown") {
            matchesElem.children[0].focus();
        }
        else if (evt.key === "Enter") {
            matchesElem.replaceChildren();
            submitItem();
        }
    });

    buttonElem.addEventListener("click", submitItem);

}