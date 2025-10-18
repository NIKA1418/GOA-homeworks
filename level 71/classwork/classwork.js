document.addEventListener("DOMContentLoaded", generateParagraph);

function generateParagraph() {

    let divElement = document.getElementById("content");

    let paragraph = document.createElement("p");

    paragraph.textContent = "ეს არის დინამიურად დამატებული პარაგრაფი!";

    divElement.appendChild(paragraph);
}

