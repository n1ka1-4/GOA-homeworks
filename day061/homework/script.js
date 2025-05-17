// 1
console.log(10 > 27);
console.log(1 > 12);
console.log(9 > "20");
console.log(20 > 28);
console.log(23 > 20);

console.log(10 < 20);
console.log(34 < 90);
console.log(10 < "28");
console.log(23 < 10);
console.log(20 < 30);

console.log(90 >= 27);
console.log(18 >= 12);
console.log(91 >= "208");
console.log(2 >= 2);
console.log(23 >= 299);

console.log(10 <= 211);
console.log(34 <= "80");
console.log(0 <= 27);
console.log(21 <= 18);
console.log(29 <= 12);

console.log(10 == 211);
console.log(`34` == "80");
console.log(0 == 27);
console.log("210" == 18);
console.log("29" == 12);

console.log(1 != 21);
console.log(34 != "122");
console.log(11 != 27);
console.log(23 != 1);
console.log(29 != "1");

console.log(111 === "211");
console.log(`34` === "80");
console.log(0 === 200);
console.log("28" === 18);
console.log("299" === 111);

console.log(12 !== 21);
console.log(911 !== "122");
console.log(11 !== 27);
console.log(23 !== 1);
console.log("29" !== "1");

// 2

// alert is used for showing a message to the user and user can only click ok button
// prompt is used for taking input from the user and user can only enter text and click ok button
// confirm is used for taking confirmation from the user and user can only click ok or cancel button

// 3

let age = confirm("Are you 18 or older?");

if (age) {
    console.log("Your are adult");
} else {
    console.log("Your are kid");
}