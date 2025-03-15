import sys
input = lambda: sys.stdin.readline().rstrip()

def check_compression(arr, x, y, size):
    first_value = arr[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != first_value: 
                return False
    return True 

def Divide(arr, x, y, size):
    if check_compression(arr, x, y, size): 
        return arr[x][y]

    mid = size // 2
    top_left = Divide(arr, x, y, mid)
    top_right = Divide(arr, x, y + mid, mid)
    bottom_left = Divide(arr, x + mid, y, mid)
    bottom_right = Divide(arr, x + mid, y + mid, mid)

    return f'({top_left}{top_right}{bottom_left}{bottom_right})'  

N = int(input())
video = [input() for _ in range(N)] 

result = Divide(video, 0, 0, N)
print(result)

# 더 효율적인 풀이
# import sys
# input = sys.stdin.readline

# n = int(input())
# board = [input().strip('\n') for _ in range(n)]

# def qt(s,x,y):
#     if s == 1:
#         return board[x][y]
#     s = s//2
#     re = ''.join([qt(s,x+dx,y+dy) for dx,dy in [(0,0),(0,s),(s,0),(s,s)]])
#     if re == '0000': return '0'
#     elif re == '1111': return '1'
#     else: return '('+re+')'

# print(qt(n,0,0))