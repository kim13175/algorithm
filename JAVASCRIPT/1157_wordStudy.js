const fs = require('fs');

const input = (process.platform === 'linux'? fs.readFileSync('/dev/stdin').toString() : 
    'Mississipi'
).trim();

// 아스키 배열 생성
const assci = new Array(26).fill(0); 

upperWord = input.toUpperCase();

// 아스키 코드 변환
console.log('A'.charCodeAt());
console.log('Z'.charCodeAt());

// 향상된 for 문 - key 값
for (let ch of upperWord){
    assci[ch.charCodeAt() - 'A'.charCodeAt()] += 1;
}

// 배열을 인수로 쓰려면 ...
const max = Math.max(...assci);

// 배열의 최대값 개수 반환
const maxCnt = assci.filter(x => x === max).length;

// 최대값이 있는 인덱스 반환
const idx = assci.indexOf(max);

// A의 아스키 코드 65를 더해야 영어 대문자 아스키 코드가 나옴
// 간단한 조건을 걸기위해 삼항연산자 사용
const result = maxCnt === 1 ? String.fromCharCode(idx + 65) : '?';

/** 
 * test print
console.log(max, maxCnt, idx, result);
*/
