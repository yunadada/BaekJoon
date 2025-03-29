const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);
const [n, ...sequence] = input;

let stack = [];
let result = [];
let num = 1; //스택에 담을 1~n의 수를 나타냄.

while (sequence.length > 0) {
  if (stack.length > 0 && stack[stack.length - 1] === sequence[0]) {
    stack.pop();
    result.push("-");
    sequence.shift();
  } else if (num <= n) {
    stack.push(num++);
    result.push("+");
  } else {
    console.log("NO");
    return;
  }
}

console.log(result.join("\n"));

// 더 효율적인 풀이
// let fs = require('fs');
// let input = fs
//   .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
//   .toString()
//   .trim()
//   .split('\n');

// const N = parseInt(input[0]);
// const target = input.slice(1).map(Number);

// let current = 1; //스택에 담을 1부터 n까지의 수를 나타냄.
// const stack = [];
// const result = [];
// let isPossible = true;

// for (let i = 0; i < N; i++) {
//   while (current <= target[i]) {
//     stack.push(current);
//     result.push('+');
//     current++;
//   }

//   if (stack[stack.length - 1] === target[i]) {
//     result.push('-');
//     stack.pop();
//   } else {
//     isPossible = false;
//     break;
//   }
// }

// isPossible ? console.log(result.join('\n')) : console.log('NO');
