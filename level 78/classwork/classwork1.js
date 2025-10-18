let myObj = {
    name: "David",
    surname: "Tezelashvili",
    academy: "GOA",
    isMentor: true,
    num: 100,
    hobbies: ["programming", "bike", "basketball"],
    favColor: "Blue"
};

let list = document.getElementById("myList");

for (let key in myObj) {
    let keyItem = document.createElement("li");
    keyItem.textContent = `Key: ${key}`;
    list.appendChild(keyItem);

    let valueItem = document.createElement("li");
    
    if (Array.isArray(myObj[key])) {
        valueItem.textContent = `Value: ${myObj[key].join(", ")}`;
    } else {
        valueItem.textContent = `Value: ${myObj[key]}`;
    }

    list.appendChild(valueItem);
}