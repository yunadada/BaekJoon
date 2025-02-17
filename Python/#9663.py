import sys
input = lambda: sys.stdin.readline().rstrip()

def Queen(row, N):
    global result

    if (row == N):
        result += 1
        return
    
    for col in range(N):
        if col in cols or row-col in LDiag or row+col in RDiag:
            continue
        else: #퀸을 배치할 수 있다면
            cols.add(col) #퀸이 위치한 열을 저장
            LDiag.add(row-col) 
            RDiag.add(row+col)
            
            Queen(row+1, N)

            #퀸을 놓을 수 없다면 백트래킹킹
            cols.remove(col)
            LDiag.remove(row-col)
            RDiag.remove(row+col)

N = int(input())

cols = set()
LDiag = set()
RDiag = set()
result = 0
Queen(0, N) 
print(result)

# 더 효율적인 풀이
# n = int(input())
# ans = 0
# row = [0] * n

# def is_promising(x):
#     for i in range(x):
#         if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
#             return False
#     return True

# def n_queens(x):
#     global ans
#     if x == n:
#         ans += 1
#         return
#     else:
#         for i in range(n):
#             # [x, i]에 퀸을 놓겠다.
#             row[x] = i
#             if is_promising(x):
#                 n_queens(x+1)

# n_queens(0)
# print(ans)