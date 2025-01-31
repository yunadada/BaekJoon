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