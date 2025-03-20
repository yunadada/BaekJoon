const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");

let [N, stone, S] = input;
stone = stone.trim().split(" ").map(Number);

let visited = new Array(Number(N)).fill(0);
visitStone(visited, stone[Number(S) - 1], Number(S) - 1);
console.log(visited.filter((item) => item === 1).length);

function visitStone(visited, mov, pos) {
  if (pos < 0 || pos >= N) {
    return;
  }
  visited[pos] = 1;

  let leftPos = pos;
  let rightPos = pos;

  //왼쪽으로 이동
  leftPos -= mov;
  visitStone(visited, stone[leftPos], leftPos);

  //오른쪽으로 이동
  rightPos += mov;
  visitStone(visited, stone[rightPos], rightPos);
}

// 더 효율적인 풀이
// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
// const n = Number(input.shift());
// const arr = input.shift().split(' ').map(Number);
// const s = Number(input.shift());
// const visited = Array(n).fill(false);
// const startIdx = s - 1;

// const bfs = (start) => {
//     const queue = [start];
//     visited[start] = true;
//     let cnt = 1;

//     while (queue.length) {
//         const cur = queue.shift();
//         const jumpDistance = arr[cur];

//         // left
//         const left = cur - jumpDistance;
//         if (left >= 0 && !visited[left]) {
//             queue.push(left);
//             visited[left] = true;
//             cnt++;
//         }
//         // right
//         const right = cur + jumpDistance;
//         if (right < n && !visited[right]) {
//             queue.push(right);
//             visited[right] = true;
//             cnt++;
//         }
//     }
//     return cnt;
// }
// console.log(bfs(startIdx));
