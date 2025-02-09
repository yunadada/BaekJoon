import sys
input = lambda: sys.stdin.readline().rstrip()

A, B = map(int, input().split())
A_SET = set(input().split())
B_SET = input().split()

for num in B_SET:
    if (num in A_SET):
        A_SET.remove(num)
    else:
        A_SET.add(num)
print(len(A_SET))

# 더 효율적인 풀이
# n,m = map(int, input().split())
# a = {i:'' for i in input().split()}
# b = input().split()
# cnt=0
# for i in range(m):
#     if b[i] in a:
#         cnt += 1

# print(len(a)+len(b)-2*cnt)