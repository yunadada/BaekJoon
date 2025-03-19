const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].trim().split(" ").map(Number);
let minCost = Infinity;
let currentCost = 0;

const arr = input.slice(1).map((line) => line.trim().split(" ").map(Number));
// console.log(JSON.stringify(arr));

for (let j = 0; j < M; j++) {
  toTheMoon(arr, 0, j, currentCost, null); //초기 방향은 null로 설정
}

console.log(minCost);

function toTheMoon(arr, i, j, money, prevDirection) {
  const direction = [-1, 0, 1]; //왼쪽아래, 아래, 오른쪽아래 방향 (행은 항상 1씩 증가)
  money += arr[i][j];

  if (i === N - 1) {
    minCost = Math.min(minCost, money);
    return;
  }

  for (let dir of direction) {
    //j값이 0인 경우 -> 왼쪽 아래 방향에 대해서는 탐색 불가능
    if (j === 0 && dir === -1) continue;
    //j값이 M-1인 경우 -> 오른쪽 아래 방향에 대해서는 탐색 불가능
    if (j === M - 1 && dir === 1) continue;

    //연속되어 같은 방향으로는 이동 불가
    if (prevDirection === -1 && dir === -1) continue;
    if (prevDirection === 0 && dir === 0) continue;
    if (prevDirection === 1 && dir === 1) continue;

    //다음 방향으로 재귀 호출
    toTheMoon(arr, i + 1, j + dir, money, dir);
  }
}
