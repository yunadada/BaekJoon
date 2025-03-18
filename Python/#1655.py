import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
max_heap_arr = []
min_heap_arr = []
mid_result = []
for _ in range(N):
    num = int(input())
    heapq.heappush(max_heap_arr, -num)

    maxHeap_len = len(max_heap_arr)
    minHeap_len = len(min_heap_arr)

    if (maxHeap_len - minHeap_len >= 2):
        heapq.heappush(min_heap_arr, -heapq.heappop(max_heap_arr))
       
    elif (minHeap_len - maxHeap_len >= 2):
        heapq.heappush(max_heap_arr, heapq.heappop(min_heap_arr))
       
    if (max_heap_arr and min_heap_arr and -max_heap_arr[0] > min_heap_arr[0]):
        maxRoot = -heapq.heappop(max_heap_arr)
        minRoot = heapq.heappop(min_heap_arr)
        heapq.heappush(min_heap_arr, maxRoot)
        heapq.heappush(max_heap_arr, -minRoot)

    mid_result.append(-max_heap_arr[0])
print('\n'.join(map(str, mid_result)))

# 더 효율적인 풀이
# import os
# from heapq import heappush, heappushpop

# def main():
#     numbers = list(map(int, os.read(0, os.fstat(0).st_size).lstrip(b"0123456789").split()))
#     answer = solve(numbers)
#     print("\n".join(map(str, answer)))

# def solve(numbers):
#     result = []
#     left, right = [], []

#     for number in numbers:
#         if not left or number <= -left[0]:
#             if len(left) <= len(right):
#                 heappush(left, -number)
#             else:
#                 heappush(right, -heappushpop(left, -number))
#         else:
#             if len(right) + 1 <= len(left):
#                 heappush(right, number)
#             else:
#                 heappush(left, -heappushpop(right, number))
#         result.append(-left[0])
#     return result
# main()