// 1
const summer = (...n) => {
    sum = 0;
    n.forEach(elm => {
        sum += elm;
    });
    return sum
};

console.log(summer(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));

// 2
let obj = {
    name: "john",
    age: 30
}
let obj2 = {
    username: "john doe",
    city: "new york"
}
let obj3 = {
    ...obj,
    ...obj2
}
console.log(obj3);

// 3
let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let arr2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
let arr3 = [...arr, ...arr2];
console.log(arr3);

