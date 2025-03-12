import sys
import heapq
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
Dict = defaultdict(deque)
heap_arr = []
for _ in range(N):
    num = int(input())
    if (num == 0):
        if (not heap_arr):
            print(0)
        else:
            value = heapq.heappop(heap_arr)
            print(Dict[value].popleft())
    else:
        heapq.heappush(heap_arr, abs(num))
        Dict[abs(num)].append(num)
        Dict[abs(num)] = deque(sorted(Dict[abs(num)]))

# 더 효율적인 풀이
# import sys
# input = sys.stdin.readline
# from heapq import heappop, heappush

# def main():
#     plus_heap = []
#     minus_heap = []
#     _, *nums = map(int, sys.stdin.buffer.read().split())
    
#     for x in nums:
#         if x > 0:
#             heappush(plus_heap, x)
#         elif x < 0:
#             heappush(minus_heap, -x)
#         else:
#             if plus_heap and minus_heap:
#                 if plus_heap[0] >= minus_heap[0]:
#                     temp = -heappop(minus_heap)
#                 else:
#                     temp = heappop(plus_heap)
#             elif plus_heap:
#                 temp = heappop(plus_heap)
#             elif minus_heap:
#                 temp = -heappop(minus_heap)
#             else:
#                 temp = 0
#             sys.stdout.write(str(temp) + '\n')

# if __name__ == '__main__':
#     main()