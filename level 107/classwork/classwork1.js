function createResolvedPromise() {
  return new Promise((resolve) => {
    resolve("resolved");
  });
}

const promise1 = createResolvedPromise();
const promise2 = createResolvedPromise();
const promise3 = createResolvedPromise();

Promise.all([promise1, promise2, promise3])
  .then((result) => {
    console.log(result); 
  });
