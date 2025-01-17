import sys
N = int(input())

dance = set()
for i in range(N):
    person1, person2 = sys.stdin.readline().rstrip().split()
    if (person1 == 'ChongChong' or person2 == 'ChongChong'):
        dance.add(person1)
        dance.add(person2)
    elif (person1 in dance and person2 not in dance):
        dance.add(person2)
    elif (person2 in dance and person1 not in dance):
        dance.add(person1)
print(len(dance))

# 더 효율적인 풀이
# import sys
# input = sys.stdin.readline

# n = int(input())
# dance = {'ChongChong'}

# for i in range(1, n+1):
#     a, b = input().rstrip().split()

#     if a in dance:
#         dance.add(b)

#     if b in dance:
#         dance.add(a)

# print(len(dance))