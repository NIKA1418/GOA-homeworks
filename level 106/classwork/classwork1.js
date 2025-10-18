function createPromise(number) {
  return new Promise((resolve, reject) => {
    if (number > 10) {
      resolve("resolve");
    } else {
      reject("reject");
    }
  });
}

createPromise(15)
  .then(result => console.log("Success:", result))
  .catch(error => console.log("Error:", error));

createPromise(5)
  .then(result => console.log("Success:", result))
  .catch(error => console.log("Error:", error));

