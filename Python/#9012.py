import sys
input = lambda: sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    stack = []
    PS = input()
    top = 0
    for ps in PS:
        if (ps == '('):
            top += 1
            stack.append('(')
        else:
            top -= 1
            if (top < 0):
                break
            stack.pop()
    if(top == 0):
        print('YES')
    else:
        print('NO')

# 더 효율적인 풀이
# import sys
# t = int(input())
# for _ in range(t):
#     ps = sys.stdin.readline()
#     while True:
#         if '()' in ps:
#             ps = ps.replace('()', '')
#         else:
#             break
#     if '(' in ps or ')' in ps:
#         print('NO')
#     else:
#         print('YES')