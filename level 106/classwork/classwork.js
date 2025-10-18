function printRandomStringAfterDelay() {
  const strings = ["ვაშლი", "ბანანი", "მსხალი", "ატამი", "საზამთრო"]; 
  const randomIndex = Math.floor(Math.random() * strings.length); 
  const selectedString = strings[randomIndex]; 

  setTimeout(() => {
    console.log(selectedString); 
  }, 3000); 
}

printRandomStringAfterDelay();

