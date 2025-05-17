// 1
// ES6 გამოვიდა 2015 წელს და მასში ბევრი ახალი ფუნქცია დაემატა
// ES6 არის JavaScript-ის ახალი ვერსია, რომელიც მოიცავს ახალ ფუნქციებს და გაუმჯობესებებს
// მაგალითად let, const, arrow functions, template literals, destructuring, modules და სხვა

// 2 
// let და const, var-ს იმიტომ არ ვიყენებთ რომ var არის global scope-ის მქონე და let, const კი block scope-ის მქონე

// 3
let listn = [1, 2, 3, 4, 5]

for (let i of listn) {
    console.log(i)
}

// 4
let obj = {
    name: 'Giorgi',
    age: 20,
    city: 'Tbilisi'
}

for (let key in obj) {
    console.log(key + ': ' + obj[key])
}

// 5
let obj1 = {
    name: 'Giorgi',
    age: 20,
}

let obj2 = {
    city: 'Tbilisi',
    country: 'Georgia'
}

console.log(Object.assign({}, obj1, obj2))

// 6
const add = (a, b) => a + b

console.log(add(2, 3))
