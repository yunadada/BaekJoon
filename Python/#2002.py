import sys

N = int(input())

front_car = set()
in_Tunnel = dict()
for _ in range(N):
    car_num = sys.stdin.readline().rstrip()
    in_Tunnel[car_num] = set(front_car)
    front_car.add(car_num)
# print(in_Tunnel)
    
out_count = 0
result = set()
for _ in range(N):
    car_num = sys.stdin.readline().rstrip()
    # print(f'터널을 나간 차량: {result}')
    for car in in_Tunnel[car_num]:
        if (car not in set(result)):
            out_count += 1
            break
    result.add(car_num)
    # print(f'현재 추월한 차량 수: {out_count}')
print(out_count)

# 더 효율적인 풀이
# import sys
# input = sys.stdin.readline

# n = int(input())
# enter = [input().strip() for _ in range(n)]

# count = 0
# for _ in range(n):
#     car = input().strip()
#     if enter[0] != car:
#         count += 1
#     enter.remove(car)
# print(count)