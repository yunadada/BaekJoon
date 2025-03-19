const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");

let maxPeople = 0;
let nowPeople = 0;
for (let i = 0; i < 4; i++) {
  let [Out, In] = input[i]
    .trim()
    .split(" ")
    .map((item) => Number(item));
  nowPeople = nowPeople - Out + In;
  if (nowPeople > maxPeople) {
    maxPeople = nowPeople;
  }
}
console.log(maxPeople);
