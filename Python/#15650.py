def DFS(num):
    global N, M
    if (num == M):
        result.append(list(sequence))
        return

    for i in range(1, N+1):
        if (sequence and (i <= sequence[-1])):
            continue
        else:
            sequence.append(i)
            DFS(len(sequence))
            sequence.pop()          

N, M = map(int, input().split())
result = []
sequence = []
DFS(0)
for seq in result:
    print(' '.join(map(str, seq)))

# 더 효율적인 풀이
# def sol(arr,m,idx):
#     if m==0:
#         print(*arr)
#         return
    
#     for i in range(idx,n+1):
#         arr.append(i)
#         sol(arr,m-1,i+1)
#         arr.pop()

# n,m=map(int,input().split())
# arr = []
# sol(arr,m,1)