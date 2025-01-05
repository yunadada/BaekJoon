def recursion(s, l, r, count):
    count += 1
    if (l >= r):
        return [1, count]
    elif (s[l] != s[r]):
        return [0, count]
    else:
        return recursion(s, l+1, r-1, count)

def isPalindrome(s, count):
    return recursion(s, 0, len(s) - 1, count)

T = int(input())
for _ in range(T):
    String = input()
    count = 0
    result = isPalindrome(String, count)
    print(result[0], result[1])