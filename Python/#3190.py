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