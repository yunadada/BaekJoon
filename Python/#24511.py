import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()  

N = int(input())
dataStructure = input().split()
data = input().split()
M = int(input())
sequence = input().split()

Queue = deque()
if '0' not in dataStructure: #자료구조에 큐가 하나도 없는 경우
       print(' '.join(sequence))
else:
    for i in range(N):
        if dataStructure[i] == '0':
            Queue.append(data[i])
    result = []
    for num in sequence: 
        Queue.appendleft(num)
        result.append(Queue.pop())
    print(' '.join(result))

# 더 효율적인 풀이
# import sys
# n = int(sys.stdin.readline())
# st = sys.stdin.readline().split()
# qs = sys.stdin.readline().split()
# m = int(sys.stdin.readline())
# x_arr = sys.stdin.readline().split()

# ans = []
# q = [qs[i] for i in range(n) if st[i] == "0"]
# q.reverse()
# print(" ".join((q + x_arr)[:m]))