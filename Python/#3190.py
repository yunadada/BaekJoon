import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
game_board = [[0] * N for _ in range(N)]

K = int(input())
for i in range(K):
    row, col = map(int, input().split())
    game_board[row-1][col-1] = 1 

change_direction_time = deque()
L = int(input())
for i in range(L):
    sec, dirc = input().split()
    change_direction_time.append([int(sec), dirc])

direction = 'E'
ROW = 1
COL = 1
now_Time = 0
snack = deque([[1, 1]])
while (True):
    if (change_direction_time and now_Time == change_direction_time[0][0]):
        if (change_direction_time[0][1] == 'D'):
            if (direction == 'E'):
                direction = 'S'
            elif (direction == 'W'):
                direction = 'N'
            elif (direction == 'N'):
                direction = 'E'
            elif (direction == 'S'):
                direction = 'W'
        elif (change_direction_time[0][1] == 'L'):
            if (direction == 'E'):
                direction = 'N'
            elif (direction == 'W'):
                direction = 'S'
            elif (direction == 'N'):
                direction = 'W'
            elif (direction == 'S'):
                direction = 'E'
        change_direction_time.popleft()
    else:
        now_Time += 1
        if (direction == 'E'):
            COL += 1
        elif (direction == 'W'):
            COL -= 1
        elif (direction == 'N'):
            ROW -= 1
        elif (direction == 'S'):
            ROW += 1
        
        if (snack and ([ROW, COL] in snack or ROW < 1 or ROW > N or COL < 1 or COL > N)): 
            print(now_Time)
            break

        if (game_board[ROW - 1][COL - 1] == 1):
            snack.append([ROW, COL])
            game_board[ROW - 1][COL - 1] = 0
        else:
            snack.append([ROW, COL])
            snack.popleft()  

# 더 효율적인 풀이
import sys
input = sys.stdin.readline

n = int(input())
board = [[0] * n for _ in range(n)]

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 2

l = int(input())
move = {}
for _ in range(l):
    a, b = input().split()
    move[int(a)] = b

def solution(n, board, move):
    time = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    snake = [[0, 0]]
    x, y, d = 0, 0, 0
    while True:
        time = time + 1
        nx = x + dx[d]
        ny = y + dy[d]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n: 
            break
        if [nx, ny] in snake: 
            break
        
        x, y = nx, ny
        snake.append([x, y])
        
        if board[x][y] == 2:
            board[x][y] = 0
        else:
            snake.pop(0)
        
        if time in move:
            if move[time] == 'D':
                d = (d + 1) % 4
            else:
                d = (d - 1) % 4
    return time

print(solution(n, board, move))