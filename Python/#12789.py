import sys
N = int(input())
num_Line = list(map(int, sys.stdin.readline().rstrip().split()))
num_Line.reverse()

LEN = len(num_Line)
result = []
wait = []

while(len(result) != LEN):
    if(len(result) == 0): #라인을 통과한 사람이 없는 경우
        if(num_Line[-1] == 1):
            result.append(num_Line.pop())
        else:
            if(len(wait) == 0):
                wait.append(num_Line.pop())
            else:
                if(wait[-1] > num_Line[-1]):
                    wait.append(num_Line.pop())
                else:
                    print('Sad')
                    sys.exit(0)
    else: #라인을 통과한 사람이 있는 경우 
        if(len(wait) == 0 and len(num_Line) != 0): #왼쪽 공간이 비어있는 경우
            if(result[-1] + 1 != num_Line[-1]):
                wait.append(num_Line.pop())
            else:
                result.append(num_Line.pop())
        elif(len(num_Line) == 0 and len(wait) != 0): #대기열이 비어있는 경우
            if(result[-1] + 1 == wait[-1]):
                result.append(wait.pop())
            else:
                print('Sad')
                sys.exit(0)
        elif(len(num_Line) != 0 and len(wait) != 0): #둘 다 비어있지 않은 경우
            if(result[-1] + 1 == num_Line[-1]):
                result.append(num_Line.pop())
            elif(result[-1] + 1 == wait[-1]):
                result.append(wait.pop())
            elif(num_Line[-1] < wait[-1]):
                wait.append(num_Line.pop())
            else:
                print('Sad')
                sys.exit(0)
    # print(f'현재 num_Line= {num_Line}, wait= {wait}, result= {result}')
# print(f'최종 num_Line= {num_Line}, wait= {wait}, result= {result}')
print('Nice')

# 더 효율적인 풀이
# import sys
# input = sys.stdin.readline
# n = int(input())
# wait = list(map(int, input().split()))
# tmp = []
# target = 1
# for i in wait:
# 	tmp.append(i)
# 	while tmp and tmp[-1] == target: # tmp 스택 하나로 비교
# 		tmp.pop()
# 		target += 1
# 	if len(tmp) > 1 and tmp[-1] > tmp[-2]:
# 		print("Sad")
# 		sys.exit()
# if tmp:
# 	print("Sad")
# else:
# 	print("Nice")