const input = require("fs").readFileSync("example.txt").toString().trim();
const stack = [];
let curValue = 1;
let result = 0;

for (let i = 0; i < input.length; i++) {
  if (input[i] === "(") {
    stack.push(input[i]);
    curValue *= 2;
  } else if (input[i] === "[") {
    stack.push(input[i]);
    curValue *= 3;
  } else if (input[i] === ")" && stack && stack[stack.length - 1] === "(") {
    if (input[i - 1] === "(") {
      result += curValue;
    }
    stack.pop();
    curValue /= 2;
  } else if (input[i] === "]" && stack && stack[stack.length - 1] === "[") {
    if (input[i - 1] === "[") {
      result += curValue;
    }
    stack.pop();
    curValue /= 3;
  } else {
    result = 0;
    break;
  }
}

if (stack.length > 0) {
  //괄호가 모두 닫히지 않은 경우
  console.log(0);
} else {
  console.log(result);
}
