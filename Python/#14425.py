import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

S = set()
for _ in range(N):
    S.add(input())

count = 0
for _ in range(M):
    text = input()
    if (text in S):
        count += 1
print(count)