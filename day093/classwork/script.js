// 1
class Animal {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    speak() {
        console.log(`hello world!`);
    }
}
class Dog extends Animal {
    constructor(name, age) {
        super(name, age);
    }
    speak() {
        console.log(`Woof!`);
    }
}

// 2
class User {
    static userCount = 0;

    constructor(name) {
        this.name = name;
        User.userCount++;
    }

    static getUserCount() {
        return User.userCount;
    }
}

const user1 = new User("john");
const user2 = new User("nika");
const user3 = new User("mari");

console.log(User.getUserCount());
