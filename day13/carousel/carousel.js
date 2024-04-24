function createCarousel(hostElemId, allImages, options) {
    // Get options, if exists.
    // let hideArrows = false;
    // let numVisible = 3;
    // if (options) {
    //     if (options.hideArrows) hideArrows = options.hideArrows;
    //     if (options.numVisible) numVisible = options.numVisible;
    // }

    let { hideArrows, numVisible } = options ?? {};  // Similar to above.

    let arrowStr = "";
    if (!hideArrows) {
        arrowStr = `
        <div class="arrow left">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"><!--!Font Awesome Free 6.5.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
                <path d="M41.4 233.4c-12.5 12.5-12.5 32.8 0 45.3l160 160c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L109.3 256 246.6 118.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-160 160z" />
            </svg>
        </div>
        <div class="arrow right">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"><!--!Font Awesome Free 6.5.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
                <path d="M278.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-160 160c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L210.7 256 73.4 118.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l160 160z" />
            </svg>
        </div>
        `
    }

    const newCarouselHTML = `
    <div class="carousel">
        ${arrowStr}
        <div class="slider"></div>
    </div>
    `;

    const hostElem = document.getElementById(hostElemId);
    hostElem.innerHTML = newCarouselHTML;

    const carouselElem = document.querySelector(`#${hostElemId} .carousel`);
    const sliderElem = document.querySelector(`#${hostElemId} .carousel .slider`);
    const leftArrow = document.querySelector(`#${hostElemId} .carousel .arrow.left`);
    const rightArrow = document.querySelector(`#${hostElemId} .carousel .arrow.right`);

    if (numVisible) {
        // Always need at least 1 on either side of the slider that is
        // not visible for smooth animation.
        if (numVisible > (allImages.length - 2)) {
            numVisible = allImages.length - 2;
        }

        carouselElem.style.width = (20 * numVisible) + "rem";
    }

    // To allow the slider to go "left" from the first image, we populate
    // the last image to the left of the first image. In other words, the
    // visible area of sliderElem is actually the 2nd, 3rd, and 4th image.
    // The 1st image is the last image from our images list to allow for
    // smooth carousel scrolling to the left. This 1st image is not
    // normally visible, but off to the left of the visible area (we
    // translated the slider -20rem from the parent carousel element,
    // and the parent carousel element has a width of 60rem, which allows
    // only 3 elements in slider to be visible.)
    insertNewHorse(allImages.at(-1), "0rem", allImages.length - 1);

    // Insert the the horses.
    for (let i = 0; i < allImages.length - 1; i++) {
        const img = allImages[i];
        insertNewHorse(img, (20 * (i + 1)) + "rem", i);
    };

    // allImages.forEach(img => {
    function insertNewHorse(newHorse, offset, idNum) {
        const newDiv = document.createElement("div");
        newDiv.id = idNum;
        newDiv.className = "horse";
        newDiv.style.backgroundImage = `url("${newHorse.url}")`;
        newDiv.style.left = offset;

        const newH = document.createElement("h3");
        newH.innerHTML = newHorse.caption;
        newDiv.appendChild(newH);

        sliderElem.appendChild(newDiv);
    }

    // If we let the user madly click the arrows, new animations will start
    // before old animations are finished, creating an odd "shuffling" kind
    // of animation. To prevent this, we're going to have the event
    // listeners do nothing for 500ms after an arrow click.
    let arrowsEnabled = true;

    function handleArrow(calcNewAmt) {
        if (arrowsEnabled) {
            arrowsEnabled = false;
            for (let i = 0; i < sliderElem.children.length; i++) {
                const item = sliderElem.children[i];
                const oldLeft = item.style.left;
                const oldAmt = parseInt(oldLeft.substring(0, oldLeft.indexOf("rem")));

                calcNewAmt(oldAmt, item);
            }
            setTimeout(() => { arrowsEnabled = true; }, 500);
        }
    }

    if (!hideArrows) {
        leftArrow.addEventListener("click", () => {
            handleArrow((oldAmt, item) => {
                const newAmt = 20 + oldAmt;
                // if (newAmt >= (sliderElem.children.length * 20)) {
                if (newAmt >= (allImages.length * 20)) {
                    item.style.zIndex = "-1";
                    item.style.left = "0rem";
                }
                else {
                    item.style.left = newAmt + "rem";
                    item.style.zIndex = "0";
                }
            });
        });

        rightArrow.addEventListener("click", () => {
            handleArrow((oldAmt, item) => {
                const newAmt = oldAmt - 20;
                if (newAmt < 0) {
                    item.style.zIndex = "-1";
                    // item.style.left = "80rem";
                    item.style.left = ((allImages.length - 1) * 20) + "rem";
                }
                else {
                    item.style.left = newAmt + "rem";
                    item.style.zIndex = "0";
                }
            });
        });
    }
}