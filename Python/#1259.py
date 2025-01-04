num = input()
while(num != '0'):
    isPalindrome = num[::-1]
    if (num == isPalindrome):
        print('yes')
    else:
        print('no')
    num = input()