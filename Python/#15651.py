def DFS(node):
    if len(sequence) == M:
        result.append(list(sequence))
        return

    for i in range(1, N+1):
        sequence.append(i)
        DFS(i)
        sequence.pop()

N, M = map(int, input().split())
result = []
sequence = []
DFS(1)
for List in result:
    print(' '.join(map(str, List)))

# 더 효율적인 풀이
# from itertools import product

# N, M = map(int, input().split())
# N = list(map(str, range(1, N+1)))
# print('\n'.join(list(map(' '.join, product(N, repeat=M)))))