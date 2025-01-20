import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
people = [i+1 for i in range(N)]
pos = 0
result = []
while (len(people) != 0):
    for i in range(K-1):
        pos = (pos + 1) % len(people)
    result.append(people.pop(pos)) 
print('<' + ', '.join(map(str, result)) + '>')

# 더 효율적인 풀이
# N, M = map(int,input().split())
# l = [n for n in range(1, N+1)]
# a = []
# r = M - 1
# while l:
#     v = l.pop(r);a.append(str(v))
#     if l:r += M-1;r %= len(l)
# print(f"<{', '.join(a)}>")

# 덱(deque) 사용 풀이
# from collections import deque
# N, K = map(int, input().split())
# person_circle = deque(range(1, N+1))
# result = []
# while len(person_circle) != 0:
#     for _ in range(K-1):
#         person_circle.append(person_circle.popleft())
#     result.append(person_circle.popleft())
# print(f"<{', '.join(map(str, result))}>")