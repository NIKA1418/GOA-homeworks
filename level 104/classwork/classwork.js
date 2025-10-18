function countKeys(obj) {
  return Object.keys(obj).length;
}

let myObject = {
  name: "Nika",
  age: 10,
  country: "Georgia"
};

console.log(countKeys(myObject)); 
