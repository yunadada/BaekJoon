import sys
while(True):
    input = sys.stdin.readline().rstrip()
    if(input == '.'):
        break
    stack = []
    top = 0
    for ps in input:
        if (ps == '(' or ps == '['):
            top += 1
            stack.append(ps)
        elif (ps == ')' or ps == ']'):
            if(top == 0):
                top -= 1
                break

            if(ps == ')'):
                if (stack[-1] == '('):
                    top -= 1
                    stack.pop()
                else:
                    break
            else:
                if(stack[-1] == '['):
                    top -= 1
                    stack.pop()
                else:
                    break
    if(top == 0):
        print('yes')
    else:
        print('no')

# 더 효율적인 풀이
# import sys
# while True:
#     s = sys.stdin.readline().rstrip()
#     if s==".":break
#     if s.count("(")!=s.count(")") or s.count("[")!=s.count("]"):print("no");continue
#     b=""
#     for i in s:
#         if i in "()[]":
#             b+=i
#     while "()" in b or "[]" in b:
#         if "()" in b:b=b.replace("()","")
#         if "[]" in b:b=b.replace("[]","")
#     if b=="":print("yes")
#     else:print("no")