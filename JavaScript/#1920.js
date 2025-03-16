const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
const N = input[0].trim();
const N_arr = new Set(input[1].trim().split(" "));
const M = input[2].trim();
const M_arr = input[3].trim().split(" ");

for (let i = 0; i < M; i++) {
  if (N_arr.has(M_arr[i])) {
    console.log(1);
  } else {
    console.log(0);
  }
}
