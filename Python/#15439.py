import sys
import math
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
print(math.perm(N, 2))