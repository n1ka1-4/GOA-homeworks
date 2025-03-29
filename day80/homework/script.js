// 1
function solution(str){
    let res = ""
    for (let i = str.length - 1; i >= 0; i--) {
      res += str[i]
    }
    return res
  }

// 2
function points(games) {
    let res = 0
    for (i of games) {
      let score = i.split(":");
      if (score[0] > score[1]) {
        res += 3
      } else if ((score[0] < score[1])) {
        res += 0
      } else {
        res += 1
      }
    }
    return res
  }

// 3
const binaryArrayToNumber = arr => {
    return parseInt(arr.map(String).join(""),2)
  };

// 4
function factorial(n) {
    if (n === 0) {
      return 1;
    } else {
      let res = 1;
      for (let i = 1; i <= n; i++) {
        res *= i;
      }
      return res;
    }
  }

// 5
function removeUrlAnchor(url){
    if (url.includes("#")) {
      return url.slice(0, url.indexOf("#"))
    } else {
      return url
    }
  }

// 6
function kebabize(str) {
    return str.split(/(?=[A-Z])/).join("-").toLowerCase().replace(/\d+/g, '')
  }