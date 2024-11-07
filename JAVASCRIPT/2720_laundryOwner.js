const fs = require('fs');
const readline = require("readline");
const terminal = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = (process.platform === "linux" ? fs.readFileSync("/dev/stdin").toString().trim().split('\n').map(Number):(
    []
));

if (input.length === 0){
    terminal.on("line", (line) => {
        input.push(Number(line));
    }).on("close", () => {
        const tests = Number(input[0]);
        let arr = [];
        for(let i = 1; i <= tests; i++){
            arr.push(Number(input[i]))
        }
        for(let i = 0; i < arr.length; i++){
            console.log(solve(arr[i]));
        }
        process.exit(0);
    })
} else{
    for (let i = 1; i < input.length; i++){
        console.log(solve(input[i]));
    }
}

function solve(total) {
    let money = [0, 0, 0, 0];
    const coins = [25, 10, 5, 1];
    for (let idx = 0; idx < money.length; idx++) {
        money[idx] += Math.floor(total / coins[idx]);
        total %= coins[idx];
    }
    return money.join(' ');
}