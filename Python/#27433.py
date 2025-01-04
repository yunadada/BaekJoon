N = int(input())

def Factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return num * Factorial(num-1)
    
result = Factorial(N)
print(result)

# num이 1이거나 0일 때 1을 출력해도 되지만, 0일 때만 1을 출력하도록해도 만족됨.