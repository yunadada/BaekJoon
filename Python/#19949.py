import sys
input = lambda:sys.stdin.readline().rstrip()

def BackTracking():
    global score, idx, result

    if (len(select) == 10):
        if (score >= 5):
            result += 1
        return
    
    for i in option:
        if (len(select) >= 2 and select[-1] == select[-2] == i):
            continue

        select.append(i) #5지선다 중 하나를 고름.
        prev_score = score
        
        if(select[idx] == answer[idx]):
            score += 1
        
        idx += 1 #위에서 답을 선택했으므로 재귀 호출 전에 인덱스를 1증가시켜서 다음 문제로 넘어감.

        BackTracking()

        score = prev_score
        select.pop()
        idx -= 1

answer = list(map(int, input().split()))
idx = 0
option = [1, 2, 3, 4, 5]
select = [] #현재 영재가 고른 정답
score = 0 #현재 영재의 점수
result = 0 #영재의 점수가 5점 이상일 경우의 수

BackTracking()
print(result)