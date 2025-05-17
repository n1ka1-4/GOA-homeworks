// 1
class Car {
    constructor(make, model) {
        this.make = make;
        this.model = model;
    }
}

const car = new Car("porsche", "911");
console.log(car.make);
console.log(car.model);

// 2
class BankAccount {
    #balance = 0;

    deposit(money) {
        if (money > 0) {
            this.#balance += money;
        }
    }

    withdraw(money) {
        if (money > 0 && money <= this.#balance) {
            this.#balance -= money;
        }
    }

    getBalance() {
        return this.#balance;
    }
}

const userAccount = new BankAccount();
userAccount.deposit(250);
userAccount.withdraw(130);
console.log(userAccount.getBalance());

// 3
class MathOperations {
    static PI = 3.14159;

    static add(a, b) {
        return a + b;
    }
}

console.log(MathOperations.add(1, 2));
console.log(MathOperations.PI);

// 4
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }

    get area() {
        return this.width * this.height;
    }

    set setWidth(value) {
        if (value > 0) {
            this.width = value;
        }
    }

    set setHeight(value) {
        if (value > 0) {
            this.height = value;
        }
    }
}

const rect = new Rectangle(5, 10);
console.log(rect.area);
rect.setWidth = 7;
rect.setHeight = 3;
console.log(rect.area);

// 5
class User {
    #password;

    #validatePassword(password) {
        return password.length >= 6;
    }

    setPassword(password) {
        if (this.#validatePassword(password)) {
            this.#password = password;
            console.log("Password is strong");
        } else {
            console.log("Password too weak");
        }
    }
}

const user = new User();
user.setPassword("12345");
user.setPassword("12345678");

// 6
class Book {
    #pages;

    constructor(title, pages) {
        this.title = title;
        this.#pages = pages;
    }

    get pages() {
        return this.#pages;
    }

    set pages(number) {
        if (value > 0) {
            this.#pages = number;
        }
    }
}

const book = new Book("harry potter", 300);
console.log(book.title);
console.log(book.pages);
book.pages = 301;
console.log(book.pages);

// 7
class Player {
    static count = 0;

    constructor(name) {
        this.name = name;
        Player.count++;
    }

    static getPlayerCount() {
        return Player.count;
    }
}

let player1 = new Player("Alice");
let player2 = new Player("Bob");

console.log(Player.getPlayerCount());

// 8
class Vehicle {
    #speed = 0;

    setSpeed(value) {
        if (value >= 0) {
            this.#speed = value;
        }
    }

    getSpeed() {
        return this.#speed;
    }
}

class Bike extends Vehicle {
    getFaster() {
        this.setSpeed(this.getSpeed() + 5);
    }
}

const bike = new Bike();
bike.getFaster();
console.log(bike.getSpeed());

// 9
class Student {
    constructor(name, grade) {
        this.name = name;
        this.grade = grade;
    }

    static compareGrades(student1, student2) {
        if (student1.grade > student2.grade) {
            return `${student1.name} has a higher grade`;
        } else if (student1.grade < student2.grade) {
            return `${student2.name} has a higher grade`;
        } else {
            return "Both students have equal grades";
        }
    }
}

const student1 = new Student("John", 79);
const student2 = new Student("Jane", 92);

console.log(Student.compareGrades(student1, student2));
