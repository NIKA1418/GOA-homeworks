function calculateOperations() {

  const input1 = prompt("შეიყვანეთ პირველი რიცხვი:");
  const input2 = prompt("შეიყვანეთ მეორე რიცხვი:");

  const num1 = parseFloat(input1);
  const num2 = parseFloat(input2);

  console.log(`ჯამი (+): ${num1 + num2}`);
  console.log(`გამოკლება (-): ${num1 - num2}`);
  console.log(`გამრავლება (*): ${num1 * num2}`);
  console.log(`გაყოფა (/): ${num1 / num2}`);
  console.log(`ხარისხი (**): ${num1 ** num2}`);
  console.log(`მთელი რიცხვით გაყოფა (//): ${Math.floor(num1 / num2)}`);
  console.log(`ნაშთი (%): ${num1 % num2}`);
}