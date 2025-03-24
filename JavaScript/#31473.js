const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
const N = Number(input[0]);
const Pink = input[1].split(" ").map(Number);
const Blue = input[2].split(" ").map(Number);

const PinkLength = Pink.reduce((acc, curr) => acc + curr, 0);
const BlueLength = Blue.reduce((acc, curr) => acc + curr, 0);

const LCM = lcm(PinkLength, BlueLength);
console.log(LCM / PinkLength, LCM / BlueLength);

function gcd(a, b) {
  return b === 0 ? a : gcd(b, a % b);
}

function lcm(a, b) {
  return Math.abs(a * b) / gcd(a, b);
}
