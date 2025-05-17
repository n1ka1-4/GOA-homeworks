// forEach
const numbers = [1, 2, 3, 4, 5];

for (let i of numbers) {
  console.log(i);
}

// map
const numbers1 = [1, 2, 3, 4, 5];

numbers1.forEach((number, index) => {
  numbers1[index] = number * 2;
});
console.log(numbers1);