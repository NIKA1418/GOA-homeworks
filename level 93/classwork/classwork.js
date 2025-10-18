let originalString = prompt("შეიყვანე საწყისი სტრინგი:");
let target = prompt("რომელი ნაწილი გინდა შეცვალო?");
let replacement = prompt("რით გსურს შეცვლა?");
let replaceType = prompt("გსურს შეცვლა მხოლოდ ერთხელ თუ ყველა შემხვედრზე? (შეიყვანეთ 'ერთხელ' ან 'ყველა')");

let result;
if (replaceType.toLowerCase() === "ერთხელ") {
  result = originalString.replace(target, replacement);
} else {
  let regex = new RegExp(target, "g");
  result = originalString.replaceAll(regex, replacement);
}


console.log("შედეგი:", result);

