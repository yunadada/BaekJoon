import sys
input = sys.stdin.readline

K = int(input())
stack = []
sum = 0
for _ in range(K):
    num = int(input())
    if (num != 0):
        stack.append(num)
        sum += num
    else:
        if (stack):
            sum -= stack.pop()
print(sum)