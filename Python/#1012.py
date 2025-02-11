import sys
sys.setrecursionlimit(2500+50)
input = lambda: sys.stdin.readline().rstrip()

def DFS(x, y):
    #상하좌우
    dx = [0, 0, -1, 1] #열
    dy = [1, -1, 0, 0] #행

    for i in range(4):
        if (0 <= y + dy[i] <= N - 1 and 0 <= x + dx[i] <= M -1 and mat[y + dy[i]][x + dx[i]] == 1):
            mat[y + dy[i]][x + dx[i]] = 0
            DFS(x + dx[i], y + dy[i])

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    mat = [[0] * M for i in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        mat[Y][X] = 1
    
    count = 0
    for x in range(M):
        for y in range(N):
            if mat[y][x] == 1:
                mat[y][x] = 0
                DFS(x, y)
                count += 1
    print(count)

# 더 효율적인 풀이
# import sys

# def solution():
#     t = int(sys.stdin.readline().rstrip())
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#     for _ in range(t):
#         m, n, k = map(int, sys.stdin.readline().split())
#         cabbages = set()
#         for _ in range(k):
#             x, y = map(int, sys.stdin.readline().split())
#             cabbages.add((x, y))

#         count = 0
#         while cabbages:
#             bug_Stomach = [cabbages.pop()]

#             while bug_Stomach:
#                 x, y = bug_Stomach.pop()
#                 for dx, dy in directions:
#                     nx, ny = x+dx, y+dy
#                     if (nx, ny) in cabbages:
#                         cabbages.discard((nx, ny))
#                         bug_Stomach.append((nx, ny))
#             count += 1
#         sys.stdout.write(str(count)+'\n')

# solution()