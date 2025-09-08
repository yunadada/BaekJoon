import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

width = []
height = []
for i in range(N):
    W, H = map(int, input().split())
    
    if (H > W):
        width.append(W)
        height.append(H)
    else:
        width.append(H)
        height.append(W)
    
max_Width = max(width)
max_Height = max(height)

print(max_Width * max_Height)