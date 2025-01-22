import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
temp_card = deque()
temp = 'a'
for i in range(N):
    temp_card.append(chr(ord(temp) + i))

tech = input().split()
real_card = dict()
for num in tech:
    if (num == '3'):
        real_card[temp_card.pop()] = N
        N -= 1
    elif (num == '2'):
        tmp = temp_card.popleft()
        real_card[temp_card.popleft()] = N
        temp_card.appendleft(tmp)
        N -= 1
    else:
        real_card[temp_card.popleft()] = N
        N -= 1

result = [real_card[key] for key in sorted(real_card)]
print(' '.join(map(str, result)))

# 더 효율적인 풀이
# from collections import deque

# n = int(input())
# skill = list(map(int, input().split()))

# deq = deque([])
# for i in range(1, n+1):
#     if skill[-1] == 1:
#         deq.appendleft(i)
#     elif skill[-1] == 2:
#         temp = deq.popleft()
#         deq.appendleft(i)
#         deq.appendleft(temp)
#     else:
#         deq.append(i)
#     skill.pop()
    
# print(" ".join(map(str, list(deq))))