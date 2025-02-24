def DFS(num):
    global N, M
    if(len(sequence) == M):
        result.add(tuple(sequence))
        return
    for i in range(num, N):
        sequence.append(SEQ[i])
        DFS(i+1)
        sequence.pop()

N, M = map(int, input().split())
SEQ = list(map(int, input().split()))
SEQ.sort()

result = set()
sequence = []
DFS(0)

result = sorted(result)
for seq in result:
    print(' '.join(map(str, seq)))

# 더 효율적인 풀이
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# nums = list(map(int, input().split()))
# nums.sort()
# answer = []

# def recur(curr, start):
#     if len(curr) == m:
#         if curr in answer:
#             return
#         answer.append(curr)
#         return
    
#     for i in range(start, n):
#         curr.append(nums[i])
#         recur(curr[:], i+1)
#         curr.pop()

# recur([], 0)
# for a in answer:
#     print(*a)