import sys
STR = sys.stdin.readline().rstrip()
BOOM = list(sys.stdin.readline().rstrip())

result = []
boom = len(BOOM)

for i in STR:
    result.append(i)
    if len(result) >= boom:
        if result[-boom:] == BOOM:
            del result[-boom:]

if (len(result) != 0):
    print(''.join(result))
else:
    print('FRULA')