def DFS():
    global N, M
    if(len(sequence) == M):
        result.add(tuple(sequence))
        return
    for i in range(N):
        sequence.append(SEQ[i])
        DFS()
        sequence.pop()

N, M = map(int, input().split())
SEQ = list(map(int, input().split()))
SEQ.sort()

result = set()
sequence = []
DFS()

result = sorted(result)
for seq in result:
    print(' '.join(map(str, seq)))

# 더 효율적인 풀이
# import sys
# from itertools import product

# input = sys.stdin.readline
# #print = sys.stdout.write

# def main():
#     N, M = map(int, input().split())
#     *arr, = list(set(map(int, input().split())))
#     arr.sort()
#     print('\n'.join(map(' '.join, product(map(str, arr), repeat=M))))
#     return

# main()