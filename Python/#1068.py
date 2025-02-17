import sys
input = lambda: sys.stdin.readline().rstrip()

def DFS(root):
    global result
    for num in Adj_mat[root]:
        DFS(num)
    if len(Adj_mat[root]) == 0: #연결된 자식 노드가 없는 리프 노드인 경우
        result += 1

N = int(input())
parent_node = list(map(int, input().split()))
Del = int(input())

Adj_mat = [[] for _ in range(N)]
for i in range(N):
    if parent_node[i] != -1:
        Adj_mat[parent_node[i]].append(i)
    else:
        root = i

# 삭제할 노드를 포함하는 부모 노드에서 미리 제거
for i in range(N):
    if Del in Adj_mat[i]:
        Adj_mat[i].remove(Del)
# print(Adj_mat)

if root == Del: #삭제할 노드가 루트인 경우 모든 노드가 삭제되므로 리프 노드 수는 1개가 됨.
    print(0)
else:
    result = 0 #리프노드 개수를 담을 전역 변수
    DFS(root)
    print(result)

# 더 효율적인 풀이
# def dfs(num, arr):
#     arr[num] = -2
#     for i in range(len(arr)):
#         if num == arr[i]:
#             dfs(i, arr)

# n = int(input())
# arr = list(map(int, input().split()))
# k = int(input())
# count = 0

# dfs(k, arr)
# count = 0
# for i in range(len(arr)):
#     if arr[i] != -2 and i not in arr:
#         count += 1
# print(count)