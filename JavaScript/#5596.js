const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");

const minguk = input[0]
  .split(" ")
  .map(Number)
  .reduce((a, b) => a + b, 0);
const manse = input[1]
  .split(" ")
  .map(Number)
  .reduce((a, b) => a + b, 0);

if (minguk === manse) {
  console.log(minguk);
} else {
  console.log(Math.max(minguk, manse));
}
