import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def BFS(i, j):
    dx = [0, 0, -1, 1] #열
    dy = [1, -1, 0, 0] #행
    SC = 0
    WC = 0
    queue = deque([(i, j)])
    while (queue):
        x, y = queue.popleft()
        visited[x][y] = True
        
        if (Adj_mat[x][y] == 'v'):
            WC += 1
        elif (Adj_mat[x][y] == 'k'):
            SC += 1
    
        for i in range(4):
            X = x + dy[i] #행
            Y = y + dx[i] #열
            if (0<= X < R and 0 <= Y < C and not visited[X][Y] and Adj_mat[X][Y] != '#'):                
                queue.append((X, Y))
                visited[X][Y] = True
    return (SC, WC)

R, C = map(int, input().split())
Adj_mat = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

sheep = 0
wolf = 0
for i in range(R):
    for j in range(C):
        if (not visited[i][j] and Adj_mat[i][j] != '#'):
            SC, WC = BFS(i, j)
            if (SC > WC):
                sheep += SC
            else:
                wolf += WC
print(sheep, wolf)

# 더 효율적인 풀이
# from sys import stdin

# def solution(R, C, graph):
#     sheep, woolf = 0, 0

#     def dfs(x, y):
#         fenceSheep, fenceWoolf = 0, 0
        
#         if graph[y][x] == 'k': fenceSheep = 1
#         if graph[y][x] == 'v': fenceWoolf = 1
#         graph[y][x] = '#'

#         stack = [(x, y)]
#         while stack:
#             x, y = stack.pop()
#             for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)): #튜플의 튜플을 순회
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] != '#':
#                     if graph[ny][nx] == 'k': fenceSheep += 1
#                     if graph[ny][nx] == 'v': fenceWoolf += 1
#                     graph[ny][nx] = '#'
#                     stack.append((nx, ny))

#         return (fenceSheep, 0) if fenceSheep > fenceWoolf else (0, fenceWoolf)
        
#     for y in range(R):
#         for x in range(C):
#             if graph[y][x] != '#':
#                 fenceSheep, fenceWoolf = dfs(x, y)
#                 sheep, woolf = sheep + fenceSheep, woolf + fenceWoolf
    
#     return sheep, woolf

# R, C = map(int,stdin.readline().split())
# graph = list(list(stdin.readline().strip()) for _ in range(R))

# sheep, woolf = solution(R, C, graph)
# print(sheep, woolf)