def DFS(num):
    global N, M
    if (len(sequence) == M):
        result.append(list(sequence))
        return  

    for i in range(num, N):
        if (visited[i] == 1):
            continue
        else:
            visited[i] = 1
            sequence.append(SEQ[i])
            DFS(i)
            visited[i] = 0
            sequence.pop()

N, M = map(int, input().split())
SEQ = list(map(int, input().split()))
SEQ.sort()
result = []
sequence = []
visited = [0] * N
DFS(0)
for seq in result:
    print(' '.join(map(str, seq)))

# 더 효율적인 풀이(1)
# import itertools
# N,M,*A=map(int,open(0).read().split())
# A.sort()
# for c in itertools.combinations(A, M):
#     print(*c)

# 더 효율적인 풀이(2)
# def combinations(c, s):
#     if len(c) == m:
#         print(*c)
#         return
    
#     for i in range(s, n):
#         c.append(seq[i])
#         combinations(c, i+1)
#         c.pop()

# n, m = map(int, input().split())
# seq = sorted(map(int, input().split()))
# combinations([], 0)