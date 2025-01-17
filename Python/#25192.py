import sys
N = int(input())

count = 0
gomgom = dict()
for i in range(N):
    chat = sys.stdin.readline().rstrip()
    if (chat == 'ENTER'):
        gomgom = dict()
    else:
        if(chat not in gomgom):
            gomgom[chat] = 1
            count += 1
print(count) 
            
# 더 효율적인 풀이
# import sys
# chat = sys.stdin.read().split("ENTER")[1:]
# ans = sum(len(set(c.split())) for c in chat)
# print(ans) 