function calculator(a, b, op) {
    if (op === "+") {
        return a + b;
    }
    if (op === "-") {
        return a - b;
    }
    if (op === "*") {
        return a * b;
    }
    if (op === "/") {
        return a / b;
    }
}

function filter(arr, func) {
    const res = [];
    arr.forEach((item) => {
        if (func(item)) {
            res.push(item);
        }
    });
    return res;
}

module.exports = { calculator, filter };

