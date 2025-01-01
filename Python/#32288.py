n = int(input())
name = list(input())
for i in range(n):
    if(name[i] == 'I'):
        print('i', end="")
    else:
        print('L', end="")

# 더 빠른 풀이
# print([*open(0)][1].swapcase())