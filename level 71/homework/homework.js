const paragraph = document.createElement("p");
paragraph.textContent = "This is a new paragraph.";
document.body.appendChild(paragraph);

const heading = document.createElement("h1");
heading.textContent = "Welcome to My Page";
const div = document.createElement("div");
div.appendChild(heading);
document.body.appendChild(div);

const image = document.createElement("img");
image.src = "https://via.placeholder.com/150"; 
image.alt = "Sample Image";
document.body.appendChild(image);

const button = document.createElement("button");
button.textContent = "Click me";
document.body.appendChild(button);

const ul = document.createElement("ul");
["Item One", "Item Two", "Item Three"].forEach(text => {
  const li = document.createElement("li");
  li.textContent = text;
  ul.appendChild(li);
});
document.body.appendChild(ul);
