def DFS(num):
    global N, M
    if (len(sequence) == M):
        print(*sequence)
        return
    
    for i in range(num, N):
        sequence.append(SEQ[i])
        DFS(i)
        sequence.pop()

N, M = map(int, input().split())
SEQ = list(map(int, input().split()))
SEQ.sort()
sequence = []
DFS(0)

# 더 효율적인 풀이(1)
# N, M = map(int, input().split())
# lst = list(map(int, input().split()))
# lst.sort()

# def bt(d, idx, arr):
#     if d == M:
#         print(' '.join(arr))
#         return
#     for i in range(idx, N):
#         arr.append(str(lst[i]))
#         bt(d+1, i, arr)
#         arr.pop()

# bt(0, 0, [])

# 더 효율적인 풀이(2)
# import itertools 

# ln, chc = map(int, input().split())
# print(*map(" ".join, itertools.combinations_with_replacement(sorted(input().split(), key = int), chc)), sep="\n")