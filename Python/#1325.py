import sys
from collections import defaultdict
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def BFS(NODE, trust, visited):
    queue = deque([NODE])
    visited[NODE-1] = 1
    trust.append(NODE)
    while queue:
        next = queue.popleft()
        visited[next-1] = 1
        trust.append(next)
        if next in adjList:
            for node in adjList[next]:
                if (visited[node-1] == 0):
                    queue.append(node)
                    visited[node-1] = 1
                    trust.append(node)
    return trust

N, M = map(int, input().split())
adjList = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    adjList[B].append(A)

maxCom = defaultdict(list)
for com in adjList:
    trust = []
    visited = [0] * N
    trust = BFS(com, trust, visited)
    maxCom[len(trust)].append(com)

result = sorted(maxCom[max(maxCom.keys())])
print(' '.join(map(str, result)))

# 더 효율적인 풀이 생각 해보기