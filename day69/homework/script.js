// 1
const h1 = document.querySelector('h1');

let interval = setInterval(() => {
    let data = new Date();
    h1.textContent = data.getMinutes() + ':' + data.getSeconds();
}, 1000);

// 2
let i = 0;

let interval2 = setInterval(() => {
    console.log(i);
    if (i > 15) {
        clearInterval(interval2);
    }
    i++;
}, 500);

// 3
setTimeout(() => {
    console.log(2);
}, 1000);

setTimeout(() => {
    console.log(1);
}, 2000);

setTimeout(() => {
    console.log(3);
}, 3000);
