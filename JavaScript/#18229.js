const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");

const [N, M, K] = input[0].split(" ").map(Number);

let firstPayer = [0, Infinity];
for (let i = 0; i < N; i++) {
  let row = input[i + 1].split(" ").map(Number);
  let sum = 0;
  let count = 0;

  for (let idx = 0; idx < M; idx++) {
    sum += row[idx];
    count += 1;
    if (sum >= K) {
      if (count < firstPayer[1]) {
        firstPayer[0] = i + 1;
        firstPayer[1] = count;
      }
      break;
    }
  }
}

console.log(firstPayer[0], firstPayer[1]);
