import sys
input = lambda: sys.stdin.readline().rstrip()

TestCase = int(input())
for _ in range(TestCase):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = input().split()
    print(N-1)