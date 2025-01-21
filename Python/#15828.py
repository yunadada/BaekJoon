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

# 더 효율적인 풀이 (접근 방법은 비슷하나, 수행 시간이나 메모리 측면에서 훨씬 효율적)
# import sys
# from collections import deque

# input = sys.stdin.readline

# def solution():
#     n = int(input())

#     buffer = deque()
#     while True:
#         packet = input().strip()
#         if packet == "-1":
#             break
#         elif packet == "0":
#             buffer.popleft()
#         elif len(buffer) == n:
#             continue
#         else:
#             buffer.append(packet)

#     if not buffer:
#         print("empty")
#     else:
#         print(" ".join(buffer))

# if __name__ == "__main__":
#     solution()