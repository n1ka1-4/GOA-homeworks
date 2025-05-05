// 1
const numbers = [-1, 4, -23, 23, 14, 3, 7, 2, 0, -5, 6, 8, 9, 5];

const isPrime = (n) => {
    if (n <= 1) {
        return false;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
};

console.log(numbers.filter((number) => isPrime(number)));

// 2
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}
const people = [
    new Person("John", 30),
    new Person("Nika", 14),
    new Person("Bob", 35),
    new Person("gio", 28),
];

console.log(people.map((person) => person.name));

// 3
const products = [
    { name: "Laptop", price: 800 },
    { name: "Mouse", price: 20 },
    { name: "Keyboard", price: 50 },
    { name: "Monitor", price: 150 },
];

console.log(products.filter((product) => product.price < 100));

// 4
const books = [
    { title: "1984", author: "George Orwell" },
    { title: "The Hobbit", author: "J.R.R. Tolkien" },
    { title: "Pride and Prejudice", author: "Jane Austen" },
];

console.log(books.map((book) => `${book.title} by ${book.author}`));

// 5
const numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];

console.log(numbers1.filter((number) => number > 10 && number % 3 === 0));

// 6
const users = [
    { name: "Alice", age: 17 },
    { name: "Bob", age: 22 },
    { name: "Charlie", age: 16 },
    { name: "Diana", age: 30 },
];

console.log(
    users.map((user) => ({
        ...user,
        isAdult: user.age >= 18,
    }))
);

// 7
const numbers2 = [100, 23, 45, 67, 89, 12, 34, 56, 78, 90, 111];

console.log(
    numbers2.filter((number) => number > 50).map((number) => number / 2)
);

// 8
const words = ["apple", "banana", "apple", "orange", "banana", "apple"];

const count = {};

words.forEach((word) => {
    count[word] = count[word] ? count[word] + 1 : 1;
});

console.log(count);

// 9
const cars = [
    { brand: { name: "Toyota" }, model: "Camry" },
    { brand: { name: "Honda" }, model: "Civic" },
    { brand: { name: "Toyota" }, model: "Corolla" },
    { brand: { name: "Ford" }, model: "Focus" },
];

console.log(cars.filter((car) => car.brand.name === "Toyota"));
