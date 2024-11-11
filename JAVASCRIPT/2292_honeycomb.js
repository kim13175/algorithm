const fs = require('fs');
const readline = require('readline');
const terminal = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = (process.platform === "linux" ? fs.readFileSync("/dev/stdin").toString().trim().split('\n').map(Number):(
    []
));

if(input.length === 0) {
    terminal.on("line", (line) => {
        input.push(Number(line));
    }).on("close", () => {
        const n = input[0];
        console.log(solve(n));
        process.exit(0);
    })
} else {
    console.log(solve(input[0]));
}

function solve(param) {
    let depth = 1;
    let level = 1;
    while (param > level) {
        level = level + (depth * 6);
        depth += 1;
    }
    return depth;
}
/*
육각형 벌집 중심 1 -> 깊이가 증가 할 때 6까지 증가
1 - 2 - 9 - 22
1 - 3 - 11 - 25
1 - 4 - 13 - 28
1 - 5 - 15 - 31
1 - 6 - 17 - 34
1 - 7 - 19 - 37
1 - 7 - 19 - 37 - 61
6 12 18 24
 */