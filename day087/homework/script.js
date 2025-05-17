// 1
    // 1)
let list = [1,2,3,4,5];
let [first, second, ...rest] = list;
    // 2)
let obj = {
    name: "John",
    age: 30,
    city: "New York"
};
let {age, ...rest1} = obj;
    // 3) 
function f(...rest) {
    console.log(rest);
};
f(1,2,3,4,5,6,7,8,9,10);

// 2
    // 1)
let list1 = [...list, 6, 7, 8, 9, 10];
    // 2)
let obj1 = {
    ...obj,
    country: "USA",
    city: "Los Angeles"
};
    // 3) and 3
function max(...rest) {
    return Math.max(...rest);
};
max(1,2,3,4,5,6,7,8,9,10)

// 4
// localstorage is used to store data in the browser

// 5
let form = document.querySelector(".form");
let name = document.querySelector("#name");

form.addEventListener("submit", function (event) {
    event.preventDefault();

    localStorage.setItem('name', JSON.stringify(name.value));

    window.location.href = "page0.html";
});


