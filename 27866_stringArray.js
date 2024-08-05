const fs = require('fs');

const input = (process.platform === 'linux' ? fs.readFileSync("dev/stdin").toString().trim().split("\n") :
    ['Sprout', '3']
);

str = input[0].split("");
findIndex = Number(input[1]);
 
console.log(str[findIndex - 1]);

console.log(typeof findIndex);