const {calculator, filter} = require('./calculator.js');


console.log(calculator(2, 3, '+'));
console.log(filter([1, 2, 3, 4], (item) => item % 2 === 0));

  