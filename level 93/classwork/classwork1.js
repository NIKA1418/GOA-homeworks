const numbers = Array.from({ length: 20 }, (_, i) => i + 1); 
const sliced = numbers.slice(4, 14); 
console.log(sliced);

const randomNumbers = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100));
const middlePart = randomNumbers.slice(1, randomNumbers.length - 1); 
console.log("Original:", randomNumbers);
console.log("Middle:", middlePart);