import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.link = None
    def __repr__(self):
        return f'[name: {self.name}, link: {self.link}]'

N = int(input())
couple_Check = dict()
for i in range(N):
    name, ring = sys.stdin.readline().rstrip().split()
    if(ring != '-'):
        Name = Node(name)
        if(ring not in couple_Check):
            couple_Check[ring] = Name
        else:
            pointer = couple_Check[ring]
            while(pointer.link != None):
                pointer = pointer.link
            pointer.link = Name
    # print(couple_Check)

feat = couple_Check.keys()
couple = 0
Couple_List = []

for feat in couple_Check:
    if(couple_Check[feat].link != None and couple_Check[feat].link.link == None):
        couple += 1
        love =  couple_Check[feat].name
        love += ' ' + couple_Check[feat].link.name
        Couple_List.append(love)

print(couple)
for i in range(couple):
    print(Couple_List[i])

# 더 효율적인 풀이
# import sys

# input = lambda: sys.stdin.readline().rstrip()

# couple_dic = {}

# for _ in range(int(input())):
#     name,ring=input().split()
#     if ring == '-':
#         continue
#     couple_dic[ring] = couple_dic.get(ring, []) + [name]
# ans=0
# for key in couple_dic:
#     if len(couple_dic[key])==2:
#         ans+=1
# print(ans)
# for key in couple_dic:
#     if len(couple_dic[key])==2:
#         print(' '.join(couple_dic[key]))