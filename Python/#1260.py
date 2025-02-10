import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M, V = map(int, input().split())

Adj_mat = [[0] * N for _ in range(N)]
for _ in range(M):
    node1, node2 = map(int, input().split())
    Adj_mat[node1-1][node2-1] = 1
    Adj_mat[node2-1][node1-1] = 1

DFS_visited = [0] * N
BFS_visited = [0] * N

def DFS(matrix, root, visited):
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            result.append(node+1)
        for i in range(len(matrix[node])-1, -1, -1):
            if matrix[node][i] == 1 and not visited[i]:
                stack.append(i)
    return result

def BFS(matrix, root, visited):
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = 1
            result.append(node+1)
            for i in range(len(matrix[node])):
                if matrix[node][i] == 1 and not visited[i]:
                    queue.append(i)
    return result

print(' '.join(map(str, DFS(Adj_mat, V-1, DFS_visited))))
print(' '.join(map(str, BFS(Adj_mat, V-1, BFS_visited))))

# 더 효율적인 풀이
# import sys
# input = sys.stdin.readline

# def dfs(v):
#     vstd[v] = True
#     smap[v].sort()
#     result.append(v)
#     for i in smap[v]:
#         if not vstd[i]:
#             dfs(i)

# def bfs(v):
#     queue = [v]
#     vstd[v] = True
#     result.append(v)
#     while queue:
#         d = queue.pop(0)
#         for i in smap[d]:
#             if not vstd[i]:
#                 queue.append(i)
#                 vstd[i] = True
#                 result.append(i)

# N,M,V = map(int,input().split())
# smap = [[] for i in range(N+1)]
# vstd = [False] * (N+1)
# result = []
# for i in range(M):
#     a,b = map(int, input().split())
#     smap[a].append(b)
#     smap[b].append(a)

# dfs(V)
# print(*result)
# result = []
# cnt = 1
# vstd = [False] * (N+1)
# bfs(V)
# print(*result)