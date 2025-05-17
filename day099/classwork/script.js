// 1
let list1 = [1, 2, 3, 4, 5];

console.log(list1.reduce((res) => {
  return res + 1;
}));

// 2
console.log(list1.reduce((res, cur) => {
    return res * cur;
  }, 1));