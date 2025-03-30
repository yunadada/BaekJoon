const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
const N = Number(input[0]);
const N_arr = input[0].split("").map(Number);
let count = 0;
console.log(countCycles(N, N_arr, count));

function countCycles(N, number, count) {
  let sum = number
    .reduce((a, b) => a + b, 0)
    .toString()
    .split("")
    .map(Number);

  let newNum = [];
  newNum.push(number.pop());
  newNum.push(sum.pop());
  count += 1;

  if (Number(newNum.join("")) === N) {
    return count;
  }

  return countCycles(N, newNum, count);
}

// 더 효율적인 풀이
// var n = require("fs").readFileSync("/dev/stdin").toString();
// var S = parseInt(n);
// var c = 0;
// while (n !== S || c == 0) {
//   n = (n % 10) * 10 + ((parseInt(n / 10) + (n % 10)) % 10);
//   c++;
// }
// console.log(c);
