N = int(input())
group_word = N

for _ in range(N):
    not_group_word = False

    word = input()
    group_or_not = set([word[0]])

    for i in range(1, len(word)):
        # print(f'현재 문자: {word[i]}')
        if (word[i] not in group_or_not):
            group_or_not.add(word[i])
        elif (word[i-1] != word[i]):
           not_group_word = True
           break
        else:
            continue
        # print(f'현재 집합: {group_or_not}')
    if (not_group_word):
        group_word -= 1
    # print(f'현재 그룹 단어: {group_word}')
print(group_word)        

# 더 효율적인 풀이
# N = int(input())
# count = 0

# for _ in range(N):
#   string = input()
#   if list(string) == sorted(string, key=string.find):
#     count += 1

# print(count)