import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

N = int(input())
arr = []
NUM = defaultdict(int)
reversed_NUM = defaultdict(list)
for i in range(N):
    num = int(input())
    arr.append(num)
    NUM[num] += 1

arr.sort()
# 산술평균 출력
SUM = sum(arr)
if (SUM < 0):
    print(-round(abs(SUM) / N))
else:
    print(round(SUM / N))

# 중앙값 출력
print(arr[N // 2])

for key, value in NUM.items():
    reversed_NUM[value].append(key)

MAX = max(reversed_NUM)
mode = 0
if (len(reversed_NUM[MAX]) != 1):
    reversed_NUM[MAX].sort()
    mode = reversed_NUM[MAX][1]
else:
    mode, = reversed_NUM[MAX]
# 최빈값 출력
print(mode)

# 범위 출력
print(arr[-1] - arr[0])

# 더 효율적인 풀이
# from sys import stdin

# def sol2108():
#     n = int(stdin.readline())
#     counts = [0]*8001
#     s = 0
#     for i in stdin:
#         num = int(i)
#         counts[num+4000] += 1

#     maxc = max(counts)
#     mode = mcnt = 0
#     idx = 0
#     med = None
#     mi, ma = 4001, -4001
#     for i in range(8001):
#         cnt = counts[i]
#         if cnt == 0:
#             continue

#         num = i-4000
#         s += num*counts[i]
#         if cnt == maxc and mcnt < 2:
#             mode = num
#             mcnt += 1
#         mi = min(mi, num)
#         ma = max(ma, num)
#         idx += counts[i]
#         if idx >= n//2+1 and med == None:
#             med = num

#     print(round(s/n), med, mode, ma-mi, sep='\n')

# if __name__ == '__main__':
#     sol2108()