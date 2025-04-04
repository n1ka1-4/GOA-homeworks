// 1
let Arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

let [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth] = Arr;
console.log(tenth);

// 2
let obj = {
    name: "John",
    city: "New York",
    country: "USA",
}

let { name, city, country } = obj;
console.log(country);

// 3
function sumer(Arr) {
    let sum = 0;
    Arr.forEach((element) => {
        sum += element;
    });
    return sum;
}
console.log(sumer([1, 2, 3, 4, 5]));
console.log(sumer([123, 23, 13, 4, 95]));

// 4
let Arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let copyOfArr1 = [...Arr1];
console.log(copyOfArr1);

// 5
let obj1 = {
    name: "John",
    age: 30,
    city: "New York",
    country: "USA",
    username: "johnDoe",
}

let { username, age, ...MInfo } = obj1;
console.log(MInfo);