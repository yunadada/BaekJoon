import sys

def Priority(operator):
    if(operator == '*' or operator == '/'):
        return 1
    else:
        return 2

infix_exp = list(sys.stdin.readline().rstrip())
# print(infix_exp)
stack = []
result = []

for i in range(len(infix_exp)):
    # print(f'현재 i: {infix_exp[i]}')
    if (infix_exp[i] == '*' or infix_exp[i] == '/' or infix_exp[i] == '+' or infix_exp[i] == '-'):
        while(stack and Priority(stack[-1]) <= Priority(infix_exp[i]) and stack[-1] != '('):
            result.append(stack.pop())
        stack.append(infix_exp[i])
    elif (infix_exp[i] == '('):
        stack.append(infix_exp[i])
    elif (infix_exp[i] == ')'):
        while (stack[-1] != '('):
            result.append(stack.pop())
        stack.pop()
    else:
        result.append(infix_exp[i])
    # print(f'현재 stack: {stack}, 현재 result: {result}')

while (len(stack) != 0):
    result.append(stack.pop())

print(''.join(result))

# 더 효율적인 풀이
# l,s=list(input()),[]
# d={'*':1,'/':1,'+':0,'-':0} -> 연산자의 우선순위를 함수가 아닌 딕셔너리로 저장
# r=[]
# for i in l:
#   if i in d:
#     while s and s[-1]!='(' and d[s[-1]]>=d[i]:
#       r.append(s.pop())
#     s.append(i)
#   elif i=='(':
#     s.append(i)
#   elif i==')':
#     while s and s[-1]!='(':
#       r.append(s.pop())
#     s.pop()
#   else:
#     r.append(i)
# while s:
#   r.append(s.pop())
# print(''.join(r))