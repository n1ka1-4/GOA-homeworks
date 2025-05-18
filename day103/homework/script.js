// 1
const promise1 = new Promise((resolve) => {
    resolve("Hello, Promise!");
});

promise1.then((message) => console.log(message));

// 2
const promise2 = new Promise((_, reject) => {
    reject("Something went wrong!");
});

promise2.catch((error) => console.error(error));

// 3
const promise3 = new Promise((resolve) => {
    setTimeout(() => {
        resolve("2 seconds have passed");
    }, 2000);
});

promise3.then((message) => console.log(message));

// 4
const promise4 = new Promise((resolve, reject) => {
    if (Math.random() > 0.5) {
        resolve("Success!");
    } else {
        reject("Failed!");
    }
});

promise4
    .then((msg) => console.log("✅", msg))
    .catch((err) => console.error("❌", err));

// 5
const promise5 = Promise.resolve(5);

promise5
    .then((num) => num * 2)
    .then((num) => num * 2)
    .then((num) => num * 2)
    .then((result) => console.log("Final result:", result));

// 6
const fakeFetch = new Promise((resolve) => {
    setTimeout(() => {
        resolve("Data fetched!");
    }, 1000);
});

fakeFetch.then((data) => console.log(data));
