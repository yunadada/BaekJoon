import sys
from collections import deque

N = int(sys.stdin.readline().rstrip()) #버퍼의 크기
router = deque()
while (True):
    packet = int(sys.stdin.readline().rstrip())
    if (packet == -1):
        break
    if (len(router) < N and packet > 0):
        router.append(packet)
    elif (packet == 0):
        router.popleft()
    # print(router)
if(router):
    print(' '.join(map(str, router)))
else:
    print('empty')
    


