N = int(input())
Short = pow(2, 15)
Int = pow(2, 31)
if(-Short <= N <= Short-1):
    print("short")
elif (-Int <= N <= Int-1):
    print("int")
else:
    print("long long")

# 더 빠른 풀이 -> 비트 연산자 사용
# 1 << n : 비트 연산을 나타내는 문법으로, 왼쪽 시프트 연산을 수행
# a=1<<15
# b=1<<31
# n=int(input())
# if -a<=n<a: print('short')
# elif -b<=n<b: print('int')
# else: print('long long')
