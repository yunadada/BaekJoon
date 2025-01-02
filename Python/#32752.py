N, L, R = map(int, input().split())
numbers = list(map(int, input().split()))
seq = sorted(numbers)
if(N == 1):
    print('1')
else:
    numbers[L-1:R] = sorted(numbers[L-1:R])
    if(seq == numbers):
        print('1')
    else:
        print('0')

# 더 효율적인 풀이
# import sys
# input = sys.stdin.readline

# n, l, r = map(int, input().split())
# A = list(map(int, input().split()))

# lp = A[:l-1]
# mp = A[l-1:r]
# rp = A[r:]
# # print(lp,mp,rp)

# ismono = True
# if lp:
#     mx = max(lp)
#     mn = min(mp)
#     if mx>mn:
#         ismono = False

# if rp:
#     mx = max(mp)
#     mn = min(rp)
#     if mx>mn:
#         ismono = False

# if ismono:
#     print(1)
# else:
#     print(0)