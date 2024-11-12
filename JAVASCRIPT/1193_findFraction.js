const fs = require('fs');
const readline = require('readline');
const terminal = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const input = (process.platform === 'linux' ? fs.readFileSync("/dev/stdin").toString().trim().split('\n') : (
    []
));

if(input.length === 0) {
    terminal.on('line', (line) => {
        input.push(Number(line));
    }).on("close", () => {
        const x = input[0];
        console.log(solve(x));
        process.exit(0);
    });
} else {
    console.log(solve(input[0]));
}

function solve(param) {
    let limit = 1;
    let n = 1;
    while (limit < param) {
        limit += n + 1;
        n += 1;
    }

    const partialNum = n - (limit - param);

    if (n % 2 === 0) {
        return `${partialNum}/${n - partialNum + 1}`;
    }
    return `${n - partialNum + 1}/${partialNum}`;
}

/*
사각형에서 대각선을 그을 경우 n 번째 대각선은 n 개의 수로 이루어짐
분모와 분자를 합할 경우 n + 1의 결과가 주어짐

1 : 1 => 1/1
2 : 2 => 1/2, 3 => 2/1
3 : 4 => 3/1, 5 => 2/2, 6 => 1/3
4 : 7 => 1/4, 8 => 2/3, 9 => 3/2, 10 => 4/1,
5 : 11 => 5/1, 12 => 4/2, 13 => 3/3, 14 => 2/4, 15 => 1/5
6 : 16 => 1/6
 */