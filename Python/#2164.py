import sys
from collections import deque

N = int(input())
CARD = deque()

if (N == 1):
    print(N)
    sys.exit()
else:
    for card in range(1, N+1):
        CARD.append(card)
    while (1):
        value = CARD.popleft()
        if (len(CARD) == 1):
            print(CARD.pop())
            sys.exit()
        CARD.append(CARD.popleft())

# 더 효율적인 풀이
# n=int(input())
# t=0
# while n>2**t:
#     t+=1
# print(int((n-2**(t-1))*2))
