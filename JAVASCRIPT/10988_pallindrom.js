const fs = require('fs');

/* boj input 
const input = fs.readFileSync("/dev/stdin").toString().trim()
*/

const input = (process.platform === 'linux' ? fs.readFileSync("/dev/stdin").toString() : 
    'noon'
).trim();

len = input.length / 2;

left_word = input.slice(0, parseInt(len));
right_word = input.slice(Number.isInteger(len) ? len : parseInt(len)+1);
right_reverse_word = right_word.split("").reverse().join("")

if (left_word === right_reverse_word) { 
    console.log(1);
}else { 
    console.log(0);
}
/**
 * test
console.log(left_word)
console.log(right_reverse_word)
**/