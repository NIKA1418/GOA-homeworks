function case_choice() {

  let userText = prompt("შეიყვანე ტექსტი:");

  let caseType = prompt("რომელ ქეისსი გსურს ტექსტის გადაყვანა (lower, l, upper, u)");

  if (caseType === "lower" || caseType === "l") {
    alert("შენი ტექსტი პატარა ასოებითაა: " + userText.toLowerCase());
  } else if (caseType === "upper" || caseType === "u") {
    alert("შენი ტექსტი დიდი ასოებითააა: " + userText.toUpperCase());
  } else {
    alert("არასწორი ქეისი აირჩიე");
  }
}

case_choice();