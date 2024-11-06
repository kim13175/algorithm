const fs = require('fs');

let input = (process.platform === 'linux'? fs.readFileSync('/dev/stdin').toString() :
        "ZZZZZ 36"
).trim();

let base = input.split(' ');
const baseList = base[0].split('');

const newList = baseList.map(item => {
    if (item >= '0' && item <= '9') return parseInt(item);
    return (item.charCodeAt(0) - 55)
})

let sum = 0;
for (let i = 0; i < newList.length; i++) {
    sum += newList[i] * (parseInt(base[1]) ** (newList.length-i-1));
}
console.log(sum);

/*
* const fs = require('fs');

let [num, base] = (process.platform === 'linux'? fs.readFileSync('/dev/stdin').toString() :
        "ZZZZZ 36"
).trim().split(' ');

// parseInt의 두 번째 인자로 진법을 직접 지정
console.log(parseInt(num, +base));

* * */