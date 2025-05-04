export function calculator(a, b, op) {
    if (op === "+") return a + b;
    if (op === "-") return a - b;
    if (op === "*") return a * b;
    if (op === "/") return a / b;
}

export function filter(arr, func) {
    return arr.filter(func);
}
