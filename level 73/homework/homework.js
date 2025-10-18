let count = 1;
let interval1 = setInterval(() => {
  console.log(count);
  if (count === 5) clearInterval(interval1);
  count++;
}, 1000);

let interval2 = setInterval(() => {
  console.log("This message appears every 2 seconds");
}, 2000);

setTimeout(() => {
  clearInterval(interval2);
}, 10000);

let colors = ["red", "blue", "green", "yellow", "purple"];
let index = 0;

let interval3 = setInterval(() => {
  document.body.style.backgroundColor = colors[index];
  index++;
  if (index === colors.length) clearInterval(interval3);
}, 3000);

let interval4 = setInterval(() => {
  let now = new Date();
  console.log(now.toLocaleTimeString());
}, 1000);

setTimeout(() => {
  clearInterval(interval4);
}, 15000);

let seconds = 0;
let interval5 = setInterval(() => {
  seconds++;
  console.log(`Timer: ${seconds}s`);
  if (seconds === 10) clearInterval(interval5);
}, 1000);

let numbers = [10, 20, 30, 40];
console.log(numbers[1]); // Logs 20

let arr = [5, 15, 25];
arr[0] = 100;
console.log(arr); // Logs [100, 15, 25]

let fruits = ["apple", "banana", "cherry"];
console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[2]);

let nums = [3, 6, 9, 12, 15];
let sum = nums[0] + nums[nums.length - 1];
console.log(sum); // Logs 18

