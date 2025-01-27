import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N, M, K = map(int, input().split())

work = []
for i in range(N):
    value = int(input())
    heapq.heappush(work, -value)

satisfy = [0]
idx = 1
while (len(work) != 0):
    root = -(heapq.heappop(work))
    today_satisfy = satisfy[idx - 1] // 2 + root
    satisfy.append(today_satisfy)
    process_work = root - M
    if (process_work > K):
        heapq.heappush(work, -process_work)
    idx += 1

END_DAY = len(satisfy) - 1
print(END_DAY)
for i in range(1, END_DAY+1):
    print(satisfy[i])

# 더 효율적인 풀이
# import sys
# import heapq

# n,m,k=map(int,sys.stdin.readline().split())
# y=0
# sat=[]

# work = [-int(sys.stdin.readline()) for _ in range(n)]
# heapq.heapify(work)

# while work :
#     big = -heapq.heappop(work)
#     y=y//2+big
#     sat.append(y)
#     big -= m

#     if big > k:
#         heapq.heappush(work, -big)
      
# print(len(sat))
# print('\n'.join(map(str, sat)))