function func1() {
    console.log("goodbye World");
}

function func2(a,b) {
    console.log(a + b);
}

function func3(a,b) {
    console.log(a * b);
}

export { func1, func2 };
export default func3;
