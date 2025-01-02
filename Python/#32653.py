import math
from functools import reduce

N = int(input())
thickness = list(map(int, input().split()))
Thickness = list(map(lambda x:x * 2, thickness))

def LCM(a, b):
    return a*b // math.gcd(a, b)

result = reduce(LCM, Thickness)
print(result)