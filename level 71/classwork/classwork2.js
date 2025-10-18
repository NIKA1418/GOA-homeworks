window.onload = function() {

    let parentDiv = document.getElementById("parentDiv");

    let oldParagraph = document.getElementById("oldParagraph");

    let newParagraph = document.createElement("p");
    newParagraph.textContent = "ეს არის ახალი პარაგრაფი!";

    parentDiv.replaceChild(newParagraph, oldParagraph);
};

