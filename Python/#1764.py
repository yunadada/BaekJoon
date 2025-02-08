import sys
input = lambda: sys.stdin.readline().rstrip()

N , M = map(int, input().split())
not_listen = set()
for _ in range(N):
    not_listen.add(input())

result = []
for _ in range(M):
    not_seen = input()
    if (not_seen in not_listen):
        result.append(not_seen)

result.sort()
print(len(result))
print('\n'.join(result))

# 더 효율적인 풀이
# import sys
# input = sys.stdin.read

# def solve():
#     data = input().split()
#     n = int(data[0])
#     m = int(data[1])
    
#     unheard = set(data[2:2+n])
    
#     both_unseen = set()
#     for name in data[2+n:]:
#         if name in unheard:
#             both_unseen.add(name)
    
#     both_unseen = sorted(both_unseen)
#     print(len(both_unseen))
#     for name in both_unseen:
#         print(name)
# solve()