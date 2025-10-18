// ეს ცვლადი გამოცხადებულია გლობალურად და ხელმისაწვდომია ყველგან
let globalVar = "I'm in the global scope";

function showGlobal() {
  console.log(globalVar); // აქ globalVar-ს წვდომა აქვს ფუნქციის გარეთ გამოცხადების გამო
}

showGlobal(); // Output: "I'm in the global scope"

function greet() {
  // ეს ცვლადი ხელმისაწვდომია მხოლოდ ფუნქციის შიგნით
  let message = "Hello from function scope";
  console.log(message);
}

greet();       // Output: "Hello from function scope"
console.log(message); // Error: message is not defined

if (true) {
  // ეს ცვლადი ხელმისაწვდომია მხოლოდ if ბლოკის შიგნით
  let blockScoped = "I exist only in this block";
  console.log(blockScoped); // Output: "I exist only in this block"
}

console.log(blockScoped); // Error: blockScoped is not defined