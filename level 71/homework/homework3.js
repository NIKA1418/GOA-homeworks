const container = document.getElementById("textContainer");
const oldP = container.querySelector("p");

const newP = document.createElement("p");
newP.textContent = "New paragraph added!";

container.replaceChild(newP, oldP);

