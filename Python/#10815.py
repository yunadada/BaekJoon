import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
have_card = set(input().split())

M = int(input())
check_card = input().split()

result = []
for card in check_card:
    if (card in have_card):
        result.append('1')
    else:
        result.append('0')
print(' '.join(result))