// შემთხვევით დავალება js გავაკეთე
// 1
function datingRange(age) {
    if (age <= 14) {
        return (
            String(parseInt(age - 0.1 * age)) +
            "-" +
            String(parseInt(age + 0.1 * age))
        );
    } else {
        return String(parseInt(age / 2 + 7)) + "-" + String(2 * (age - 7));
    }
}

// 2
function twoHighest(arr) {
    if (arr.length > 1) {
        let x = Math.max(...arr);
        let max = 0;
        for (let i of arr) {
            if (i > max && i != x) {
                max = i;
            }
        }
        return [x, max];
    } else {
        return arr;
    }
}
