import sys
input = lambda: sys.stdin.readline().rstrip()
word = input()
croatia = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

for cro in croatia:
    word = word.replace(cro,'/')
print(len(word))