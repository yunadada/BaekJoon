import sys
num = int(sys.stdin.readline())
sequence = sys.stdin.readline().rstrip().split()

stack = []
result = []
for i in range(len(sequence)-1, -1, -1):
    if(len(stack) == 0):
        result.append('-1')
        stack.append(sequence[i])
    elif (int(stack[-1]) > int(sequence[i])):
        result.append(stack[-1])
        stack.append(sequence[i])
    else:
        while (stack and int(stack[-1]) <= int(sequence[i])):
            stack.pop()
        if(len(stack) == 0):
            result.append('-1')
            stack.append(sequence[i])
        else:
            result.append(stack[-1])
            stack.append(sequence[i])

result.reverse()
print(' '.join(result))

# 더 효율적인 풀이
# import sys

# N = int(sys.stdin.readline().rstrip())
# A = list(map(int, sys.stdin.read().split()))
# stack = [0] * N
# top = 1
# ans = [-1] * N

# for i in range(1, N):
#     while top != 0 and A[stack[top - 1]] < A[i]:
#         ans[stack[top - 1]] = A[i]
#         top -= 1
#     stack[top] = i
#     top += 1

# sys.stdout.write(" ".join(map(str, ans)))