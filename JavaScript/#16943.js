const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(" ");
const [A, B] = input;

let visited = new Array(A.length).fill(0);
let C = "";
let result = "";

if (A.length > B.length) {
  console.log(-1);
} else {
  // 정수 A의 각 자릿수를 내림차순으로 정렬
  const sort_A = A.split("").sort((a, b) => b - a);
  Back(sort_A);
  if (result) {
    console.log(result);
  } else {
    console.log(-1);
  }
}

function Back(sort_A) {
  if (A.length === C.length) {
    if (Number(C) < Number(B)) {
      result = C;
      return;
    } else {
      return;
    }
  }

  for (let i = 0; i < A.length; i++) {
    if (visited[i] === 1) {
      continue;
    } else {
      visited[i] = 1;
      C += sort_A[i];

      Back(sort_A);
      if (result) {
        if (result[0] === "0") {
          result = "";
        }
        break;
      }

      visited[i] = 0;
      C = C.slice(0, -1);
    }
  }
}
