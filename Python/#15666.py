def DFS(num):
    global N, M
    if(len(sequence) == M):
        result.add(tuple(sequence))
        return
    for i in range(num, N):
        sequence.append(SEQ[i])
        DFS(i)
        sequence.pop()

N, M = map(int, input().split())
SEQ = list(map(int, input().split()))
SEQ.sort()

result = set()
sequence = []
DFS(0)

result = sorted(result)
for seq in result:
    print(' '.join(map(str, seq)))

# 더 효율적인 풀이
# from itertools import combinations_with_replacement as cwr

# N, M = map(int, input().split())
# A = sorted(input().split(), key=int)
# print('\n'.join(' '.join(c) for c in dict.fromkeys(cwr(A, M))))