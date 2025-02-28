import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
N_num = list(map(int, input().split()))
haveCard = dict()
for card in N_num:
    if card in haveCard:
        haveCard[card] += 1
    else:
        haveCard[card] = 1

M = int(input())
M_num = list(map(int, input().split()))
result = []
for card in M_num:
    if card in haveCard:
        result.append(haveCard[card])
    else:
        result.append(0)
print(' '.join(map(str, result)))