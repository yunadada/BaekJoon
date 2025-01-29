import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()
N = int(input())

heap_arr = []
for _ in range(N):
    num = int(input())
    if (num == 0):
        if (not heap_arr):
            print(0)
        else:
            print(-heapq.heappop(heap_arr))
    else:
        heapq.heappush(heap_arr, -num)