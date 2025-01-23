import sys
from collections import deque
N = int(input())
ballon = list(map(int, sys.stdin.readline().rstrip().split()))
Ballon = deque(enumerate(ballon, start=1))

result = []
while (Ballon):
    num, step = Ballon.popleft() 
    # print(f'현재 풍선 번호: {num}, 이동할 단계: {step}')
    result.append(num)
    if (step > 0):
        Ballon.rotate(-(step - 1))
    else:
        Ballon.rotate(-(step))
    # print(f'현재 풍선 위치들: {Ballon}')
print(' '.join(map(str, result)))

# 더 효율적인 풀이
# def main():
#     N = int(input())  # 카드의 개수 입력 받기
#     cards = list(map(int, input().split()))  # 카드 값 입력 받기
#     balloons = list(range(N))  # 카드 위치를 나타내는 리스트 생성
#     ind = 0  # 현재 인덱스
#     result = []

#     while cards:
#         result.append(balloons.pop(ind) + 1)  # 해당 카드의 원래 위치 기록
#         mov = cards.pop(ind)  # 현재 위치의 이동 값

#         if not cards:
#             break

#         if mov > 0:
#             ind = (ind + mov - 1) % len(cards)
#         else:
#             ind = (ind + mov) % len(cards)

#     print(" ".join(map(str, result)))  # 결과 출력

# if __name__ == "__main__":
#     main()