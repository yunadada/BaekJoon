const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");

const T = Number(input[0]);
let idx = 1;

for (let test_case = 0; test_case < T; test_case++) {
  const [n, k, t, m] = input[idx++].split(" ").map(Number);
  const serverLog = input
    .slice(idx, idx + m)
    .map((item) => item.split(" ").map(Number));

  const teamMap = new Map(
    Array.from({ length: n }, (_, i) => [
      i + 1,
      {
        scores: Array(k).fill(0),
        attempts: 0,
        lastTime: 0,
        totalScore: 0,
      },
    ])
  );

  for (const [index, [teamId, problemNum, score]] of serverLog.entries()) {
    const team = teamMap.get(teamId);
    const problemIdx = problemNum - 1;

    //더 높은 점수만 반영
    if (score > team.scores[problemIdx]) {
      team.scores[problemIdx] = score;
    }
    team.attempts += 1;
    team.lastTime = index + 1;
  }

  //총점 계산
  for (const team of teamMap.values()) {
    team.totalScore = team.scores.reduce((a, b) => a + b, 0);
  }

  //정렬
  const sorted = [...teamMap.entries()].sort((a, b) => {
    const A = a[1],
      B = b[1];

    if (B.totalScore !== A.totalScore) return B.totalScore - A.totalScore; //총점이 높은 팀이 앞으로(내림차순)
    if (A.attempts !== B.attempts) return A.attempts - B.attempts; //총점이 같으면 풀이 제출 횟수가 적은 팀이 앞으로(오름차순)
    return A.lastTime - B.lastTime; //둘 다 같으면 마지막 제출 시간이 빠른 팀이 앞으로(오름차순)
  });

  const myRank = sorted.findIndex(([id]) => id === t) + 1; //배열의 요소를 순회하며 당신 팀을 찾음(위치는 0부터 시작하는 인덱스를 반환하므로 실제 순위는 +1한 값임.)
  console.log(myRank);

  idx += m;
}
