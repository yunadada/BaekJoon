import sys
import heapq

class Node:
    def __init__(self, prio, id, time):
        self.prio = prio
        self.id = id
        self.time =time

    def __repr__(self):
        return f'Node[prio: {self.prio}, id: {self.id}, time: {self.time}]'

    def __lt__(self, other):
        if (self.prio == other.prio):
            return self.id < other.id
        return self.prio < other.prio

input = lambda: sys.stdin.readline().rstrip()
T, n = map(int, input().split())

heap_arr = []
for i in range(n):
    id, time, prio = map(int, input().split())
    node = Node(-prio, id, time)
    heapq.heappush(heap_arr, node)

end_time = 0
result = []
while (end_time < T):
    process = heapq.heappop(heap_arr)
    result.append(process.id)
    end_time += 1
    process.prio += 1 
    process.time -= 1
    if (process.time > 0):
        heapq.heappush(heap_arr, process)
print('\n'.join(map(str, result)))

# 더 효율적인 풀이
# import sys
# from heapq import heappop, heappush
# from collections import defaultdict
# input = sys.stdin.readline

# t, n = map(int, input().split())
# hq, rest = [], [0] * 1000001
# for _ in range(n):
#     ids, id_rest, prior = map(int, input().split())
#     heappush(hq, (-prior, ids))
#     rest[ids] = id_rest

# use = [-1] * t
# time = 0
# while time < t and hq:
#     prior, ids = heappop(hq)
#     use[time] = ids
#     rest[ids] -= 1

#     if rest[ids]:
#         heappush(hq, (prior+1, ids))

#     time += 1

# print('\n'.join(map(str, use[:time])))