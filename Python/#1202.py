import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
jewel = []
for _ in range(N):
    weight, price = map(int, input().split())
    heapq.heappush(jewel, (weight, price))
# print(f'현재 보석 최소힙: {jewel}')

bag = []
for _ in range(K):
    bag_weight = int(input())
    heapq.heappush(bag, bag_weight)
# print(f'현재 가방 최소힙: {bag}')

tmp_jewel = []
sum = 0
while(bag):
    now_bag = heapq.heappop(bag)
    while (jewel and now_bag >= jewel[0][0]):
        jewel_price = heapq.heappop(jewel)
        heapq.heappush(tmp_jewel, -jewel_price[1])
    # print(f'{now_bag} 가방에 대한 현재 임시 보석 배열: {tmp_jewel}')

    if (tmp_jewel):
        max_price = -heapq.heappop(tmp_jewel) 
        sum += max_price
    # print(f'임시 보석 배열: {tmp_jewel}')
    # print(f'현재 누적 값: {sum}')
print(sum)

# 더 효율적인 풀이
# from heapq import heappop, heappush
# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# n, k = map(int, input().split())
# jewels = defaultdict(list)

# for _ in range(n):
#     m, v = map(int, input().split())
#     jewels[m].append(v)

# bags = sorted(int(input()) for _ in range(k))

# res = 0
# pq = []
# available = sorted(jewels.keys())
# i = 0

# for c in bags:
#     while i < len(available) and available[i] <= c:
#         for j in jewels[available[i]]:
#             heappush(pq, -j)
#         i += 1
#     if pq:
#         res -= heappop(pq)
# print(res)