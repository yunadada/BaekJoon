import sys

N = int(input())
stack = []
for i in range(N):
    case = sys.stdin.readline().rstrip().split()
    if(case[0] == '1'):
        stack.append(int(case[1]))
    elif(case[0] == '2'):
        if(len(stack) != 0):
            value = stack.pop()
            print(value)
        else:
            print(-1)
    elif(case[0] == '3'):
        print(len(stack))
    elif(case[0] == '4'):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    else:
        if(len(stack) != 0):
            print(stack[-1])
        else:
            print(-1)