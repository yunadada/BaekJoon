const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
const [N, M] = input.shift().split(" ").map(Number);
const numArr = input.shift().split(" ").map(Number);

const prefixSum = [0];
for (let i = 0; i < N; i++) {
  prefixSum[i + 1] = prefixSum[i] + numArr[i];
}

let result = [];
for (let i = 0; i < M; i++) {
  const [I, J] = input[i].split(" ").map(Number);
  const sum = prefixSum[J] - prefixSum[I - 1];
  result.push(sum);
}

console.log(result.join("\n"));
