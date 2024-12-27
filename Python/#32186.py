from collections import deque

def Swap(first, last):
    return last, first

N, K = map(int, input().split())
sequence = deque(list(map(int, input().split())))
sum = 0
for i in range(N//2):
    first = sequence.popleft()
    last = sequence.pop()

    if(first == last): continue

    if(first < last):
        first, last = Swap(first, last)

    q, r = divmod(first-last, K)
    addValue = q + r
    sum += addValue
print(sum)

