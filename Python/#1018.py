import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
black = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
white = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

arr = []
for _ in range(N):
    arr.append(input())

Min = 64 
for i in range(N - 8 + 1): #행 
    for j in range(M - 8 + 1): #열 
        count = 0 #다시 칠해야하는 칸의 개수를 담는 변수
        first_color = arr[i][j] #현재 8×8 부분의 첫 번째 칸 색

        for row in range(i, i + 8):
            if first_color == 'B':
                expected = black if row % 2 == 0 else white  #첫 칸이 'B'면 짝수행의 경우 black, 홀수행의 경우 white
            else:
                expected = white if row % 2 == 0 else black  #첫 칸이 'W'면 짝수행의 경우 white, 홀수행의 경우 black

            for col, color in enumerate(expected): #해당 열에 와야하는 색깔과 인덱스를 한 번에 가져오기 위해 enumerate 사용
                actual_col = j + col
                if arr[row][actual_col] != color:
                    count += 1 #체스판의 패턴과 맞지 않는다면 다시 칠해야하므로 카운트 증가
        Min = min(Min, count, 64-count)
print(Min)