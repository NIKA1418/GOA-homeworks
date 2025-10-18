<button id="colorButton">change background color</button>

document.getElementById("colorButton").addEventListener("click", function() {
    let userColor = prompt("შეიყვანეთ ფერი ( red, blue, #ff5733):");

    if (userColor) {
        this.style.backgroundColor = userColor;
    }
});

