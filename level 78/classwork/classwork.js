let total = 0;
let number;

do {
  number = Number(prompt("შეიყვანე რიცხვი:"));
  total += number;
} while (total <= 100);

alert("ჯამი გადაცდა 100-ს: " + total);