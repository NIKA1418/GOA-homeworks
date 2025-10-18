const myArray = ["მზიანი", "წვიმიანი", 5, 12, true, false];

for (const item of myArray) {
  if (typeof item === "string") {
    console.log(item);
  } else if (typeof item === "number") {
    console.log(item + 10);
  } else if (typeof item === "boolean") {
    console.log(!item);
  }
}