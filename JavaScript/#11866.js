const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(" ");
const [N, K] = input;

let Deque = Array.from({ length: Number(N) }, (_, i) => i + 1);
let count = 0;
let result = [];

while (Deque.length !== 0) {
  let value = Deque.shift();
  count += 1;

  if (count === Number(K)) {
    result.push(value);
    count = 0;
  } else {
    Deque.push(value);
  }
}
console.log(`<${result.join(", ")}>`);

// 더 효율적인 풀이
// function solution(N, K) {
//   var answer = '';
//   var circleArray = Array(N);
//   var head = 0;

//   for (var i = 0; i < N; i++) {
//     circleArray[i] = i + 1;
//   }

//   while (circleArray.length > 0) {
//     head += K - 1;
//     head %= circleArray.length;
//     if (answer) answer += ', ';
//     answer += circleArray[head];
//     circleArray.splice(head, 1);
//   }

//   return '<' + answer + '>';
// }

// var input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
// console.log(solution(parseInt(input[0]), parseInt(input[1])));
