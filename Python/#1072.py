import sys
from fractions import Fraction
input = lambda: sys.stdin.readline().rstrip()

X, Y = map(int, input().split())
Z = Fraction(Y, X)

if (int(Z*100) >= 99):
    print(-1)
    sys.exit()
# print(f'초기 승률: {Z}')

left = 1
right = X

lower_bound = 0
while (left <= right):
    game = X
    win = Y
    mid = (left + right) // 2
    # print(f'현재 mid값: {mid}')

    game += mid
    win += mid
    winRate = Fraction(win, game)
    # print(f'변경된 승률: {winRate}')
    
    if (int(winRate*100) > int(Z*100)):
        lower_bound = mid
        right = mid - 1
    else:
        left = mid + 1
    # print(f'현재 right 포인터: {right}, 현재 left 포인터: {left}')
    # print(f'현재 lower_bound: {lower_bound}')
print(lower_bound)

# 더 효율적인 풀이
# x, y = map(int, input().split())
# z = int(100 * y / x)

# st = 0
# ed = x

# if z >= 99:
#   print(-1)
# else:
#   while st <= ed:
#     mid = (st + ed) // 2
#     if int(100 * (y + mid) / (x + mid)) > z:
#       ed = mid - 1
#     else:
#       st = mid + 1
#   print(st)