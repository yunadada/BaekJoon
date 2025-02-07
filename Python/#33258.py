import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
teacher = list(map(int, input().split()))
L = int(input())

left = 1
right = 1000000000

while (left <= right):
    Like = 0
    mid = (left + right) // 2
    # print(f'현재 mid: {mid}')
    for math in teacher:
        if (mid >= math):
            Like += mid
        else:
            Like += 2*(mid - math)
    # print(f'호감도: {Like}')
    if (Like >= L):
        right = mid - 1
    else:
        left = mid + 1
    # print(f'현재 left: {left}, 현재 right: {right}')
print(left)