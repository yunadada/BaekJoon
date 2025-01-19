import sys

N = int(sys.stdin.readline().rstrip())
problem_List = dict()
reverse_problem_List = dict()

for _ in range(N):
    P, L = map(int, sys.stdin.readline().rstrip().split())
    if (L not in problem_List):
        problem_List[L] = {P}
    else:
        problem_List[L].add(P)
    reverse_problem_List[P] = L
# print(problem_List)
# print(reverse_problem_List)

M = int(sys.stdin.readline().rstrip())
for _ in range(M):
    command = sys.stdin.readline().rstrip().split()
    if (command[0] == 'recommend'):
        if (command[1] == '1'):
            if (problem_List.keys()):
                hard = max(problem_List.keys())
                if (len(problem_List[hard]) == 1):
                    # print('>> 추천 문제 출력')
                    print(*problem_List[hard])
                else:
                    # print('>> 추천 문제 출력')
                    print(max(problem_List[hard]))
        else:
            if (problem_List.keys()):
                easy = min(problem_List.keys())
                if (len(problem_List[easy]) == 1):
                    # print('>> 추천 문제 출력')
                    print(*problem_List[easy])
                else:
                    # print('>> 추천 문제 출력')
                    print(min(problem_List[easy]))
    elif (command[0] == 'solved'):
        if (int(command[1]) in reverse_problem_List):
            # 난이도 저장
            level = reverse_problem_List[int(command[1])]
            # 해당 난이도에 대한 문제가 1개 있는 경우 난이도 키 자체를 삭제
            if (len(problem_List[level]) == 1):
                del problem_List[level]
            # 해당 난이도에 대한 문제가 여러 개 있는 경우 키에 대한 집합 에서 해당 문제를 삭제제
            else:
                problem_List[level].remove(int(command[1]))
            del reverse_problem_List[int(command[1])]
            
            # print(problem_List)
            # print(reverse_problem_List)
    else:
        if (int(command[2]) not in problem_List):
            problem_List[int(command[2])] = {int(command[1])}
        else:
            problem_List[int(command[2])].add(int(command[1]))
        reverse_problem_List[int(command[1])] = int(command[2])
        # print(problem_List)
        # print(reverse_problem_List)