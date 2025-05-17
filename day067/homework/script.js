// 1

function summer(arr) {
    let sumOf = 0;
    for (let i of arr) {
        sumOf += i;
    }
    return sumOf;
}

console.log(summer([1, 2, 3, 4, 5]));

// 2

function min_max(arr) {
    return [Math.min(...arr), Math.max(...arr)];
}

console.log(min_max([1, 2, 3, 4, 5]));

// 3

function size(n) {
    let ll = [];
    for (let i = 0; i < n; i++) {
        ll.push(Math.floor(Math.random() * 100));
    }
    return ll;
}

console.log(size(5));

// 4

function square(arr) {
    let sq = [];
    for (let i of arr) {
        sq.push(i ** 2);
    }
    return sq;
}

console.log(square([1, 2, 3, 4, 5]));

// 5

function rounder(n) {
    return [Math.floor(n), Math.ceil(n), Math.round(n)];
}

console.log(rounder(3.14));

