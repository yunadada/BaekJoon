import sys
N = int(input())
Majak = sys.stdin.readline().rstrip().split()

Change = dict()
for i in range(N):
    if(Majak[i] not in Change):
        Change[Majak[i]] = 1
    else:
        Change[Majak[i]] += 1
        if(Change[Majak[i]] >= 5):
            print(i+1)
            sys.exit()
            
print(0)
