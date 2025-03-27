const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("");
const A_Length = input.filter((str) => str !== "b").length;
let minValue = Infinity;
for (let i = 0; i < input.length; i++) {
  let text = [];
  for (let j = 0; j < A_Length; j++) {
    const idx = (i + j) % input.length;
    text.push(input[idx]);
  }
  minValue = Math.min(minValue, text.filter((str) => str !== "a").length);
}
console.log(minValue);
