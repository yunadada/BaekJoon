def DFS():
    global M
    if (len(sequence) == M):
        result.append(list(sequence))
        return
    for i in range(len(SEQ)):
        if (visited[i] == 1):
            continue
        else:
            visited[i] = 1
            sequence.append(SEQ[i])
            DFS()
            visited[i] = 0
            sequence.pop()

N, M = map(int, input().split())
SEQ = sorted(map(int, input().rstrip().split()))
result = []
sequence = []
visited = [0] * N
DFS()
for seq in result:
    print(' '.join(map(str, seq)))

# 더 효율적인 풀이
# from itertools import permutations
# N, M = map(int, input().split())
# print('\n'.join(map(' '.join, permutations(sorted(input().split(), key=int), M))))