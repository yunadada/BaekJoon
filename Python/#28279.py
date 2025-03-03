import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
DEQUE = deque()
for _ in range(N):
    command = list(map(int, input().split()))
    if (command[0] == 1):
        DEQUE.appendleft(command[1])
    elif (command[0] == 2):
        DEQUE.append(command[1])
    elif (command[0] == 3):
        if (DEQUE):
            print(DEQUE.popleft())
        else:
            print(-1)
    elif (command[0] == 4):
        if (DEQUE):
            print(DEQUE.pop())
        else:
            print(-1)
    elif (command[0] == 5):
        print(len(DEQUE))
    elif (command[0] == 6):
        if (DEQUE):
            print(0)
        else:
            print(1)
    elif (command[0] == 7):
        if (DEQUE):
            print(DEQUE[0])
        else:
            print(-1)
    elif (command[0] == 8):
        if (DEQUE):
            print(DEQUE[-1])
        else:
            print(-1)