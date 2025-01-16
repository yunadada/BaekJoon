import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
sequence = sys.stdin.readline().rstrip().split()

counter = Counter(sequence)
num_count = {key: (value, key) for key, value in counter.items()}

stack = []
result = []
for i in range(len(sequence)-1, -1, -1):
    if(len(stack) == 0):
        result.append('-1')
        stack.append(num_count[sequence[i]])
    elif(stack[-1][0] > num_count[sequence[i]][0]):
        result.append(stack[-1][1])
        stack.append(num_count[sequence[i]])
    else:
        while(stack and stack[-1][0] <= num_count[sequence[i]][0]):
            stack.pop()
        if(len(stack) == 0):
            result.append('-1')
            stack.append(num_count[sequence[i]])
        else:
            result.append(stack[-1][1])
            stack.append(num_count[sequence[i]])

    # print(f'현재 result= {result}')
    # print(f'현재 stack = {stack}')
    # print('-------------------------')
result.reverse()
print(' '.join(result))

# 더 효율적인 풀이 생각해보기