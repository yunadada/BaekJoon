def Calculate(N):
    if (N == 0):
        return 0
    elif (N == 1):
        return 1
    else:
        return Calculate(N-1) + Calculate(N-2)
N = int(input())
print(Calculate(N))

