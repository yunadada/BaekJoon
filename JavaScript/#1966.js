const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const caseNum = parseInt(input[0]);

let idx = 1;
for (let i = 0; i < caseNum; i++) {
  const [N, M] = input[idx++].trim().split(" ").map(Number);
  let priority = input[idx++].trim().split(" ").map(Number);
  PrintQueue(N, M, priority);
}

function PrintQueue(N, M, priority) {
  if (N === 1) {
    console.log(1);
  } else {
    let result = [];
    let priority_with_idx = priority.map((value, index) => [value, index]);
    // console.log(JSON.stringify(priority_with_idx));

    while (priority_with_idx.length) {
      let POP = priority_with_idx.shift();
      let maxValue = priority_with_idx.reduce(
        (max, tuple) => Math.max(max, tuple[0]),
        -Infinity
      );

      if (POP[0] < maxValue) {
        priority_with_idx.push(POP);
      } else {
        result.push(POP[1]); // 인덱스 추가
        if (POP[1] === M) {
          console.log(result.length); // 원하는 위치 출력
          return;
        }
      }
    }
  }
}

// 더 효율적인 풀이
// function count(N, M, Q) {
//   var counter = 1;
//   var index;
//   while ((index = Q.indexOf(Math.max.apply(null, Q))) !== M) {
//     for (var i = 0; i < index; i++) {
//       Q.push(Q.shift());
//     }
//     Q.shift();
//     M = (((M - index - 1) % N) + N) % N;
//     N--;
//     counter++;
//   }
//   return counter;
// }

// var fs = require("fs");
// var input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// for (var i = 1; i <= (input.length - 1) / 2; i++) {
//   console.log(
//     count(
//       parseInt(input[2 * i - 1].split(" ")[0]),
//       parseInt(input[2 * i - 1].split(" ")[1]),
//       input[2 * i].split(" ").map(function (item) {
//         return parseInt(item);
//       })
//     )
//   );
// }
