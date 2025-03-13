const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
var WORD = new Map();

for (let i = 1; i <= N; i++) {
  let word = input[i].trim();
  let LENGTH = word.length;

  if (WORD.has(LENGTH)) {
    if (!WORD.get(LENGTH).includes(word)) {
      WORD.get(LENGTH).push(word);
    }
  } else {
    WORD.set(LENGTH, [word]);
  }
  //  WORD.get(LENGTH).sort();
}

WORD.forEach((value, key) => {
  value.sort();
});

// 키 값을 기준으로 오름차순 정렬
const sortedMap = new Map([...WORD.entries()].sort((a, b) => a[0] - b[0]));
// console.log(JSON.stringify([...sortedMap.entries()]));
for (let value of Array.from(sortedMap.values()).flat()) {
  console.log(value);
}

// 더 효율적인 풀이
// const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n").slice(1);

// const words = new Set(input);

// console.log(
//   [...words]
//     .sort((a, b) => {
//       if (a.length === b.length) {
//         let i = 0;
//         let result = 0;

//         while (true) {
//           if (a.charCodeAt(i) !== b.charCodeAt(i)) result = a.charCodeAt(i) - b.charCodeAt(i);
//           if (result) break;
//           i++;
//           if (i > a.length - 1) break;
//         }

//         return result;
//       }

//       return a.length - b.length;
//     })
//     .join("\n")
// );
