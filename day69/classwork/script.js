// 1
let data = new Date();

// 2
console.log(data);
console.log(data.getDate());
console.log(data.getMonth());
console.log(data.getFullYear());
console.log(data.getHours());
console.log(data.getMinutes());
console.log(data.getSeconds());
console.log(data.getMilliseconds());
console.log(data.getDay());
console.log(data.getDate());

// 3
const h1 = document.querySelector('h1');

let interval = setInterval(() => {
    let data = new Date();
    h1.textContent = data.getHours() + ':' + data.getMinutes() + ':' + data.getSeconds();
}, 1000);