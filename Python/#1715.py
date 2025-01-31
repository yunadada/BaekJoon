import sys
import heapq
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
card_list = []
for _ in range(N):
    card = int(input())
    heapq.heappush(card_list, card)

sum = 0
while (len(card_list) > 1):
    first_card = heapq.heappop(card_list)
    second_card = heapq.heappop(card_list)
    card_check = first_card + second_card
    sum += card_check
    heapq.heappush(card_list, card_check)
    
print(sum)
    
# 더 효율적인 풀이
# import sys

# input = sys.stdin.readline

# n = int(input())
# piles = [int(input()) for _ in range(n)]

# if n == 1:
#     print(0)
# else:
#     piles.sort()
#     ans = piles[0] + piles[1]
#     new_piles = [ans]
#     p1 = 2
#     p2 = 0
#     while p1 < n:
#         compared = 0
#         if piles[p1] < new_piles[p2]:
#             compared += piles[p1]
#             p1 += 1
#         else:
#             compared += new_piles[p2]
#             p2 += 1
#         if p1 == n:
#             compared += new_piles[p2]
#             p2 += 1
#         elif p2 == len(new_piles):
#             compared += piles[p1]
#             p1 += 1
#         elif piles[p1] < new_piles[p2]:
#             compared += piles[p1]
#             p1 += 1
#         else:
#             compared += new_piles[p2]
#             p2 += 1
#         ans += compared
#         new_piles.append(compared)
#     for i in range(len(new_piles) - p2 - 1):
#         compared = new_piles[p2 + 2 * i] + new_piles[p2 + 2 * i + 1]
#         ans += compared
#         new_piles.append(compared)
#     print(ans)