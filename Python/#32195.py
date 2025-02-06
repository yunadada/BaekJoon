import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
Foul = 0
battedBall = []
for _ in range(N):
    x, y = map(int, input().split())
    if (y >= 0 and y >= x and y >= -x):
        battedBall.append(int((x**2 + y**2)))
    else:
        Foul += 1
battedBall.sort()

Q = int(input())
for _ in range(Q):
    distance = int(input())
    left = 0
    right = len(battedBall) - 1
    while (left <= right):
        mid = (left + right) // 2
        if (battedBall[mid] > int(distance**2)):
            right = mid - 1
        else:
            left = mid + 1
        # print(f'현재 중간값: {mid}, left: {left}, right: {right}')
    Infield = left
    HomeRun = len(battedBall) - Infield
    print(Foul, Infield, HomeRun)