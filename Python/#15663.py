def DFS():
    global N, M
    if (len(sequence) == M):
        result.add(tuple(sequence))
        return
    for i in range(N):
        if (visited[i] == 1):
            continue
        else:
            sequence.append(SEQ[i])
            visited[i] = 1
            DFS()
            sequence.pop()
            visited[i] = 0

N, M = map(int, input().split())
SEQ = list(map(int, input().split()))
SEQ.sort()

result = set()
sequence = []
visited = [0] * N
DFS()

result = sorted(result)
for seq in result:
    print(' '.join(map(str, seq)))

# 더 효율적인 풀이(1)
# from itertools import permutations

# N, M = map(int, input().split())
# A = sorted(input().split(), key=int)
# print('\n'.join(' '.join(c) for c in dict.fromkeys(permutations(A, M)).keys()))

# 더 효율적인 풀이(2)
# def backtracking(p):
#     if len(p) == m and tuple(p) not in seq_set:
#         print(*p)
#         seq_set.add(tuple(p))
#         return
    
#     for i in range(n):
#         if not used[i]:
#             p.append(seq[i])
#             used[i] = True
#             backtracking(p)
#             used[i] = False
#             p.pop()

# n, m = map(int, input().split())
# seq = sorted(map(int, input().split()))

# seq_set = set()

# used = [False]*n
# backtracking([])