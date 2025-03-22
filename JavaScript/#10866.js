const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
const N = Number(input[0]);

let Deque = [];
let result = [];
for (let i = 1; i <= N; i++) {
  let command = input[i].trim().split(" ");

  switch (command[0]) {
    case "push_front":
      Deque.unshift(Number(command[1]));
      break;
    case "push_back":
      Deque.push(Number(command[1]));
      break;
    case "pop_front":
      if (Deque.length === 0) {
        result.push(-1);
      } else {
        result.push(Deque.shift());
      }
      break;
    case "pop_back":
      if (Deque.length === 0) {
        result.push(-1);
      } else {
        result.push(Deque.pop());
      }
      break;
    case "size":
      result.push(Deque.length);
      break;
    case "empty":
      if (Deque.length === 0) {
        result.push(1);
      } else {
        result.push(0);
      }
      break;
    case "front":
      if (Deque.length === 0) {
        result.push(-1);
      } else {
        result.push(Deque[0]);
      }
      break;
    case "back":
      if (Deque.length === 0) {
        result.push(-1);
      } else {
        result.push(Deque[Deque.length - 1]);
      }
      break;
  }
}
console.log(result.join("\n"));
