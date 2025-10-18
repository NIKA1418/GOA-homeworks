function removeChildElement() {

    let parentDiv = document.getElementById("parentDiv");

    let childDiv = document.getElementById("childDiv");

    if (childDiv) {
        parentDiv.removeChild(childDiv);
    }
}

