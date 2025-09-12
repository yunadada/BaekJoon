import sys
input = lambda: sys.stdin.readline().rstrip()

while(1):
    first, second = map(int, input().split())
    
    if (first == 0 and second == 0):
        break
    
    if((first < second) and (second % first == 0)):
        print("factor")
    elif((first > second) and (first % second == 0)):
        print("multiple")
    else:
        print("neither")
        