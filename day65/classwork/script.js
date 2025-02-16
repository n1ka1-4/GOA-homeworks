// 1


// 2
function player(name, age, country, score, method) {
    this.name = name;
    this.age = age;
    this.country = country;
    this.score = score;
    this.method = method;
}
function method() {
    this.score += 100;
}

const player1 = new player('John', 25, 'USA', 50, method);

// 3

// functions are not in class of str or int or float or any other data type but methods are in class of str or int or float or any other data type and because of this we need to write into function as a parameter the object of the class in which the method is present

// 4
function Person(name, age, country) {
    this.name = name;
    this.age = age;
    this.country = country;
}

const person1 = new Person('John', 25, 'USA');

// 5
function car(name, model, price, horsepower, method) {
    this.name = name;
    this.model = model;
    this.price = price;
    this.horsepower = horsepower;
    this.method = method;
}
function method() {
    this.method += 100;
}

const car1 = new car('Honda', 'Civic', 20000, 100, method);




