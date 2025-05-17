// 1
class BankAccount {
    #balance = 0;

    deposit(amount) {
        this.#balance += amount;
    }

    withdraw(amount) {
        if (amount <= this.#balance) {
            this.#balance -= amount;
        } else {
            console.log("you dont have money");
        }
    }

    getBalance() {
        return this.#balance;
    }
}

const bank = new BankBankount();
bank.deposit(100);
bank.withdraw(30);
console.log(bank.getBalance());

// 2
class Author {
    constructor(name) {
        this.name = name;
    }
}

class Book {
    constructor(title, author) {
        this.title = title;
        this.author = author;
    }

    getDetail() {
        console.log(`${this.title} by ${this.author.name}`);
    }
}

const author = new Author("nika");
const book = new Book("harry potter", author);
book.getDetail();

// 3
class Employee {
    #salary;

    constructor(name, salary) {
        this.name = name;
        this.#salary = salary;
    }

    getSalary() {
        return this.#salary;
    }
}

class Manager extends Employee {
    constructor(name, salary, department) {
        super(name, salary);
        this.department = department;
    }

    getInfo() {
        console.log(
            `name:${this.name} department:${
                this.department
            } salary:${this.getSalary()}`
        );
    }
}

const manager = new Manager("nika", 5000, "programming");
manager.getInfo();
