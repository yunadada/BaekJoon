import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Queue = deque()
for i in range(N):
    command = input().split()
    if (command[0] == 'push'):
        Queue.append(command[1])
    elif (command[0] == 'pop'):
        if (Queue):
            print(Queue.popleft())
        else:
            print('-1')
    elif (command[0] == 'size'):
        print(len(Queue))
    elif (command[0] == 'empty'):
        if (Queue):
            print('0')
        else:
            print('1')
    elif (command[0] == 'front'):
        if (Queue):
            print(Queue[0])
        else:
            print('-1')
    elif (command[0] == 'back'):
        if (Queue):
            print(Queue[-1])
        else:
            print('-1')