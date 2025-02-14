import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def BFS(y, x):
    #상하좌우
    dx = [0, 0, -1, 1] #열
    dy = [1, -1, 0, 0] #행
    queue = deque([(y, x)])
    size = 0
    while (queue):
        Y, X = queue.popleft()
        size += 1
        for i in range(4):
            bx = X + dx[i]
            by = Y + dy[i]
            if (0 <= bx < N and 0 <= by < M and Adj_mat[by][bx] == 0):
                queue.append((by, bx))
                Adj_mat[by][bx] = -1
    return size

M, N, K = map(int, input().split())
Adj_mat = [[0] * N for _ in range(M)]

for _ in range(K):
    LUX, LUY, RTX, RTY = map(int, input().split())
    for row in range(M-RTY, M-LUY):
        for col in range(LUX, RTX):
            Adj_mat[row][col] = 1

result = []
count = 0
for y in range(M): #행
    for x in range(N): #열
        if (Adj_mat[y][x] == 0):
            Adj_mat[y][x] = -1
            result.append(BFS(y, x))
            count += 1
print(count)
result.sort()
print(' '.join(map(str, result)))