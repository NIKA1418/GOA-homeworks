function workingOnPromise(myString) {
  const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
      if (myString.length > 5) {
        resolve(" წარმატება! სთრინგი საკმარისად გრძელია: " + myString);
      } else {
        reject(" შეცდომაა! სთრინგი ძალიან მოკლეა: " + myString);
      }
    }, 1000); 
  });

  promise
    .then((message) => {
      console.log("Then:", message);
    })
    .catch((error) => {
      console.log("Catch:", error);
    });
}

workingOnPromise("hello");   //მოკლე
workingOnPromise("javascript");  //გრძელი
workingOnPromise("code");  //მოკლე