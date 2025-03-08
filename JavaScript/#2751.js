const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
const [n, ...arr] = input;

arr.sort(function (a, b) {
  return a - b;
});

console.log(arr.join("\n"));

// 더 효율적인 풀이
// let input = require("fs")
// .readFileSync("/dev/stdin")
// .toString()
// .trim()
// .split("\n")
// .map(Number);

// let N = input.shift(); //배열의 첫 번째 요소를 꺼내어 N에 저장
// let result = ""; //결과 문자열을 저장할 변수
// let arr = new Array(2000001).fill(0); //범위가 -1,000,000 ~ 1,000,000 이므로 가능한 값의 총 개수는 2,000,001개임.

// for(let i = 0; i < N; i++){
//     arr[input[i]+1000000]++; //배열의 인덱스는 음수가 될 수 없기 때문에 +1000000을 하여 음수를 양수로 변환해준다.
// }

// for(let i = 0; i < arr.length; i++){
//     if(arr[i] === 1) result += `${i-1000000}\n`;
// }

// console.log(result.trim());
