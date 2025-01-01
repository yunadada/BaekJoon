import sys

N = int(input())
num = list(map(int, input().split()))
check = [0] * 4
recip = list(input())

recip_len = len(recip)
if not (recip[0] == recip[recip_len-1] == 'a'):
    print('No')
    sys.exit(0)

for i in range(recip_len-1):
    if(recip[i] == recip[i+1]):
        print('No')
        sys.exit(0)

    if(recip[i] == 'a'):
        check[0] += 1
        if(check[0] > num[0]):
            print('No')
            sys.exit(0)
    elif(recip[i] == 'b'):
        check[1] += 1
        if(check[1] > num[1]):
            print('No')
            sys.exit(0)
    elif(recip[i] == 'c'):
        check[2] += 1
        if(check[2] > num[2]):
            print('No')
            sys.exit(0)
    elif(recip[i] == 'd'):
        check[3] += 1
        if(check[3] > num[3]):
            print('No')
            sys.exit(0)
print('Yes')

