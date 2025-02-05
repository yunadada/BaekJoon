import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    full_exp = N * (N + 1) // 2

    left = 1
    right = N
    while (left <= right):
        mid = (left + right) // 2
        # print(f'현재 중앙값: {mid}')
        if (mid * (mid + 1) <= full_exp):
            left = mid + 1
        else:
            right = mid - 1
        # print(f'[현재 left 포인터: {left}, 현재 right 포인터 : {right}]')
    print(left)

# 더 효율적인 풀이
# import sys
# import math

# testCase = int(sys.stdin.readline().rstrip())

# for case in range(testCase):
#     N = int(sys.stdin.readline().rstrip())

#     total_exp = N*(N+1) // 2

#     print((1 + math.isqrt(1 + 4 * total_exp)) // 2)