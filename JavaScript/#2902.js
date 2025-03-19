const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("-");

let shortAlgorithm = "";
for (let i = 0; i < input.length; i++) {
  shortAlgorithm += input[i].trim()[0];
}
console.log(shortAlgorithm);

// 더 효율적인 풀이
// console.log(
//   require("fs")
//     .readFileSync("/dev/stdin")
//     .toString()
//     .split("-")
//     .map(function (e) {
//       return e[0];
//     })
//     .join("")
// );
