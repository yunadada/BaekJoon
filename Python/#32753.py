N, K = map(int, input().split())
if(N == 1):
    for i in range(K):
        print('1', end=" ")
elif (N == 2 and K == 1):
    for i in range(1, N+1):
        print(i, end =" ")
else:
    print('-1')

# 더 효율적인 풀이
# N, K = map(int, input().split())
# if N == 1:
#     print("1 " * N * K)
# elif N == 2 and K == 1:
#     print("1 2")
# else:
#     print(-1)