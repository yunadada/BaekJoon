def DFS(num):
    global M
    if (len(sequence) == M):
        print(*sequence)
        return
    for i in range(N):
        sequence.append(SEQ[i])
        DFS(i)
        sequence.pop()

N, M = map(int, input().split())
SEQ = list(map(int, input().split()))
SEQ.sort()
sequence=[]
DFS(SEQ[0])

# 더 효율적인 풀이(라이브러리 사용)
# from itertools import product

# n, m = map(int, input().split())
# seq = sorted(map(int, input().split()))
# print('\n'.join(map(' '.join, product(map(str, seq), repeat=m))))