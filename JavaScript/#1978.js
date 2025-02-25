// /dev/stdin
const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(/\s/);
let [n, ...arr] = input;
n = parseInt(n);
arr = arr.map((item) => parseInt(item));

var prime_count = 0;
for (var i = 0; i < n; i++) {
  if (isPrime(arr[i])) prime_count += 1;
}
console.log(prime_count);

function isPrime(n) {
  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n % 2 == 0 || n % 3 == 0) return false;

  for (var i = 5; i * i <= n; i += 6) {
    if (n % i == 0 || n % (i + 2) == 0) return false;
  }

  return true;
}
