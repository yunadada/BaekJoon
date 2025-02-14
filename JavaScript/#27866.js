const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(/\r?\n/);

const idx = parseInt(input[1]) - 1;
console.log(input[0][idx]);
