import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

H = int(input())
N, Q = map(int, input().split())

attack_card = list(map(int, input().split()))
Card_Attack = []
now_attack = 0
for card in attack_card:
    heapq.heappush(Card_Attack, card)
    now_attack += card

plus_card = []
for _ in range(Q):
    plus_card.append(int(input()))

result = [-1] * (Q+1)
for i in range(Q+1):
    while (now_attack >= H):
        if (Card_Attack and now_attack - Card_Attack[0] >= H):
            delete = heapq.heappop(Card_Attack)
            now_attack -= delete
        else: #더이상 뺄 수 있는 카드가 없는 경우
            result[i] = len(Card_Attack)
            break
    if (i != Q):
        heapq.heappush(Card_Attack, plus_card[i]) #카드를 하나씩 추가
        now_attack += plus_card[i] #추가된 카드에 적힌 공격력만큼 현재 공격력도 증가시킴.
print('\n'.join(map(str, result)))

# 더 효율적인 풀이 추가