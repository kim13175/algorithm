const fs = require("fs");
const readline = require("readline");
const terminal = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = (process.platform === "linux" ? fs.readFileSync("/dev/stdin").toString().trim().split(" ").map(Number) : (
    []
));

if (input.length === 0) {
    terminal.on("line", (line) => {
        line = line.split(" ");
        line.forEach((value) => {
            input.push(Number(value));
        });

    }).on("close", () => {
        const a = input[0];
        const b = input[1];
        const v = input[2];
        console.log(solve(a, b, v));
        process.exit(0);
    });
} else {
    console.log(solve(input[0], input[1], input[2]));
}

function solve(up, down, height) {
    if ((height - down) % (up - down) === 0) return Math.floor((height - down) / (up - down));
    return Math.floor((height - down) / (up - down) + 1);
}

/*
23(나무높이) - 3(내려감) - 1 / {10(올라감) - 3(내려감) : 하루 + 1} = 7
- 나무 높이에서 내려가는 위치 만큼
7 + (10 - 3) = 14
14 + (10 - 3) = 21
- 이미 10을 올라가면 도착해있음
 */