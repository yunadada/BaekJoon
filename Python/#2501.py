import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
divisors = set()
for i in range(1, int(N**0.5) + 1):
    if (N % i == 0):
        divisors.add(i)
        divisors.add(N // i)

arr = sorted(divisors)
if (K > len(arr)):
    print(0)
else:
    print(arr[K-1])
        