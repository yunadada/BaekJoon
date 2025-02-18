def DFS(num):
    global N, M
    if (num == M):
        result.append(list(sequence))
        return 

    for i in range(N):
        if (visited[i] == 1):
            continue
        else:
            visited[i] = 1
            sequence.append(i+1)
            DFS(len(sequence))

            #백트래킹
            visited[i] = 0
            sequence.pop()

N, M = map(int, input().split())
visited = [0] * N
sequence = []
result = []
DFS(0)
for seq in result:
    print(' '.join(map(str, seq)))

# # 더 효율적인 풀이
# from itertools import permutations
# n, m = map(int, input().split())
# print('\n'.join(map(' '.join, permutations(map(str, range(1, n+1)), m))))