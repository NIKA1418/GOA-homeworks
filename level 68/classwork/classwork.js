function forConditions() {
    let userNum = Number(prompt("Enter number:"));

    if (userNum < 18) {
        console.log("You are not adult");
    } else if (userNum < 65) {
        console.log("You are adult and not old");
    } else if (userNum <= 113) {
        console.log("You are retired");
    } else {
        console.log("Lie");
    }
}

