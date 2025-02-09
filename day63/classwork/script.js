// 1
let num = Number(prompt("Enter a number: "));

if (num > 90 && num <= 100) {
    console.log("A");
} else if (num > 80 && num <= 90) {
    console.log("B");
} else if (num > 70 && num <= 80) {
    console.log("C");
} else if (num > 60 && num <= 70) {
    console.log("D");
} else if (num > 50 && num <= 60) {
    console.log("E");
} else {
    console.log("F");
}

// 2

let age = Number(prompt("Enter a age: "));

if (age < 13) {
    console.log("Your are kid");
} else if (age >= 13 && age <= 17) {
    console.log("Your not adult yet");
} else {
    console.log("Your are adult");
}

// 3

// we use () to check the condition and {} to execute the code block but in python we use : and indentation to execute the code block also in python we use elif instead of else if and print instead of console.log last one in js we use let to declare a variable but in python we use nothing

// 4
let i = 0;

while (i <= 100) {
    console.log(i);
    i++;
}

// 5
for (let i = 5; i <= 10; i++) {
    console.log(i);
}