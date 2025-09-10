import sys
import math
import bisect
input = lambda: sys.stdin.readline().rstrip()

def calculateSize(n):
    d = 12 * n - 3
    if d < 0:
        return 0
    
    sqrt_d = math.sqrt(d)   
    k = (3 + sqrt_d) / 6    
    
    return int(math.floor(k))  

N, M = map(int, input().split())
problem_levels = sorted(map(int, input().split()))
player_levels = list(map(int, input().split()))
answer = []

for player in player_levels:
    count = bisect.bisect_right(problem_levels, player)
    canSolve = calculateSize(count)
    answer.append(canSolve)
    
print(' '.join(map(str, answer)))

# 더 효율적인 풀이
# import sys

# input = sys.stdin.readline

# def solution():
#     input()
#     cnt_list = [0]*1000002
#     for a in map(int, input().split()):
#         cnt_list[a] += 1
#     k = p = 1
#     for i in range(1, 1000002):
#         cnt_list[i] += cnt_list[i-1]
#         if cnt_list[i-1] >= p:
#             k += 1
#             p = 3*k*(k-1)+1
#         cnt_list[i-1] = k-1
#     res = [cnt_list[b] for b in map(int, input().split())]
#     print(' '.join(map(str, res)))

# solution()