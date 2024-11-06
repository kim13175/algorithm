const fs = require('fs');
const [num, base] = (process.platform === "linux"? fs.readFileSync('/dev/stdin').toString():
    "60466174 36"
).trim().split(" ");

const baseSplitList = [];
const integerBase = parseInt(base);
let integerNum = parseInt(num);

while(integerNum >= integerBase){
    let variable = integerNum % integerBase;
    baseSplitList.push(variable);
    integerNum = parseInt(integerNum / integerBase);
}

baseSplitList.push(integerNum);
baseSplitList.reverse();

const resultList = baseSplitList.map((element) => {
    if (element >= 10) {
        element += 55;
        return String.fromCharCode(element);
    }
    return element;
})

const result = resultList.join("");

console.log(result);

/*
11 % 2 = 1
11 - (2**0) = 10
10 % 2 = 0
10 - (2**1) = 8
8 % 2 = 0
8 - (2**2) = 4
 */