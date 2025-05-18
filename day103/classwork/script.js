// 1
// Promise არის JavaScript-ის ობიექტი, რომელიც წარმოადგენს მომავალში ასინქრონუlად დასრულებულ ოპერაციას წარმატებით (resolve) ან შეცდომით (reject).

// 2
const resolvedPromise = new Promise((resolve) => {
    setTimeout(() => {
        resolve("2 seconds have passed");
    }, 2000);
});

resolvedPromise.then((data) => console.log(data));

// 3
const rejectedPromise = new Promise((_, reject) => {
    setTimeout(() => {
        reject("error");
    }, 2000);
});

rejectedPromise.catch((error) => console.error(error));

// 4
const randomPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        const success = Math.random() > 0.5;

        if (success) {
            resolve(" success");
        } else {
            reject(" failed");
        }
    }, 2000);
});

randomPromise
    .then((result) => console.log(result))
    .catch((error) => console.error(error));
