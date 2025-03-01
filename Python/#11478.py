import sys
input = lambda: sys.stdin.readline().rstrip()

def subString(String):
    substring = set()
    for start in range(len(String)):
        for end in range(start+1, len(String)+1):
            print(start,end)
            substring.add(String[start:end])
    return substring 

S = input()
print(len(subString(S)))