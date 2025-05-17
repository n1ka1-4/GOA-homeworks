// 1
function sum (numbers) {
    let res = 0
    for (i of numbers) {
      res += i;
    }
    return res
};

// 2
function findAverage(array) {
    let res = 0
    for (i of array) {
      res += i;
    }
    if (res > 0) {
      return res / array.length
    } else {
      return 0
    }
};

// 3
function countBy(x, n) {
    let range = [];
    for (let i = x; i < x * n + 1; i += x) {
      range.push(i);
    }
    return range;
};

// 4
const reverseSeq = (n) => {
    let range = [];
    for (let i = n; i >= 1; i--) {
      range.push(i);
    }
    return range;
};

// 5
function findMissingLetter(array) {
    for (let i = 0; i < array.length - 1; i++) {
  
      if (array[i].charCodeAt(0) !== array[i + 1].charCodeAt(0) - 1) {
        return String.fromCharCode(array[i].charCodeAt(0) + 1);
      }
    }
}

