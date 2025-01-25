import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
top = list(map(int, input().split()))
Top = {key: idx + 1 for idx, key in enumerate(top)}

stack = []
result = [0] * N
for i in Top:
    while (stack):
        if (stack[-1] > i):
            result[Top[i]-1] = Top[stack[-1]]
            break
        else:
            stack.pop()
    stack.append(i)
    # print(f'stack: {stack}')
    # print(f'result: {result}')
print(' '.join(map(str, result)))    
    
# 더 효율적인 풀이
# from sys import stdin
# input = stdin.readline
# n = int(input())
# towers = map(int, reversed(input().split()))
# stack = []
# ans = [0]*n
# for idx, height in enumerate(towers):
#     if stack and stack[-1][1] < height:
#         while stack and stack[-1][1] < height:
#             ans[stack[-1][0]] = n - idx
#             stack.pop()
#     stack.append((n - idx - 1, height))
# print(" ".join(map(str, ans)))