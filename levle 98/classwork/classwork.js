const numbers = [12, 45, 67, 23, 89, 34, 56, 78, 10, 21];

const firstGreaterThan50 = numbers.find(num => num > 50);
console.log("First number greater than 50:", firstGreaterThan50);

const firstDivisibleBy7 = numbers.find(num => num % 7 === 0);
console.log("First number divisible by 7:", firstDivisibleBy7);
