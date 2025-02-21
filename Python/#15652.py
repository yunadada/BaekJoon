def DFS(num):
    global N, M
    if (len(sequence) == M):
        result.append(list(sequence))
        return
    for i in range(num, N+1):
        sequence.append(i)
        DFS(i)
        sequence.pop()

N, M = map(int, input().split())
result = []
sequence = []
DFS(1)
for seq in result:
    print(' '.join(map(str, seq)))

#더 효율적인 풀이
# from itertools import combinations_with_replacement
# N, M = map(int, input().split())
# print("\n".join(map(" ".join, combinations_with_replacement([chr(ord('1') + i) for i in range(N)], M))))