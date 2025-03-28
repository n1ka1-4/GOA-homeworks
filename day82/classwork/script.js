let person = {
    name: "nika",
    age: 25,
    lastName: "kakabadze",
}
localStorage.setItem("person", JSON.stringify(person))


let person1 = JSON.parse(localStorage.getItem("person"))

console.log(person1.name);

person1.name = "giorgi"

localStorage.setItem("person", JSON.stringify(person1))
