Input = list(input().split())
value = {key: index for index, key in enumerate(Input)}
Fvalue = {index: key for index, key in enumerate(Input)}
fA, fB = input().split()

a = []
b = []
for i in fA:
    a.append(value[i])

for i in fB:
    b.append(value[i])

A = int(''.join(map(str, a)))
B = int(''.join(map(str, b)))
AB = str(A+B)

result = []
for i in AB:
    i = int(i)
    result.append(Fvalue[i])

result = int(''.join(result))
print(result)

# 더 효율적인 풀이
# S = list(input().split())
# a, b = input().split()
# A, B = '', ''
# for i in a:
#     A += str(S.index(i))
# for i in b:
#     B += str(S.index(i))
# for i in str(int(A) + int(B)):
#     print(S[int(i)], end = '')
    
