const fs = require("fs");
const readline = require("readline");
const terminal = readline.createInterface({
    input : process.stdin,
    output : process.stdout
});

let input = (process.platform === "linux" ? fs.readFileSync("/dev/stdin").toString().trim().split('\n') : (
    []
));

terminal.on("line", (line) => {
    input.push(Number(line));
}).on("close", () => {
    const n = Number(input[0]);
    console.log(solve(n));
    process.exit(0);
})

function solve(n) {
    let dp = Array(n+1).fill(0);
    dp[1] = 3;
    for (let i = 2; i <= n; i++) {
        dp[i] = dp[i-1] + Math.pow(2, i-1);
    }
    return Math.pow(dp[n], 2);
}

/*
0 => 4
1 => (2 + 1) * 3
2 => (3 + 2^(2-1)) * 5
3 => (5 + 4) * 9
4 => (9 + 8) * 17
5 => (17 + 16) * 33
 */