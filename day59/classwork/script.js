let num1 = Number(prompt("Enter the first number: "));
let num2 = Number(prompt("Enter the second number: "));

console.log(num1 + num2);


let name = String(prompt("Enter your name: "));

console.log("Hello " + name + "!");

const submit = document.getElementById("submit");

submit.addEventListener("click", function() {
    let name = document.getElementById("name").value;
    console.log("Hello " + name + "!");
});
