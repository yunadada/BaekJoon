import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
money_time = list(map(int, input().split()))

min_time = 0
result = 0
money_time.sort(reverse=True)
while(money_time):
    MIN = money_time.pop()
    min_time += MIN
    result += min_time
print(result)