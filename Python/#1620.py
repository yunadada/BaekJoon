import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
POKETMON = dict()
for i in range(1, N+1):
    name = input()
    POKETMON[name] = i
    POKETMON[str(i)] = name

for _ in range(M):
    question = input()
    print(POKETMON[question])

# 더 효율적인 풀이
#import sys
# input = sys.stdin.read

# def main():
#     data = input().splitlines()

#     num_poke, num_q = map(int, data[0].split())
#     pokemons = data[1 : num_poke + 1]

#     poke_dict = {name: idx + 1 for idx, name in enumerate(pokemons)}

#     output = []
#     for q in data[num_poke + 1 :]:
#         if q.isdigit():  
#             output.append(pokemons[int(q) - 1])
#         else: 
#             output.append(str(poke_dict[q]))

#     sys.stdout.write("\n".join(output) + "\n")

# if __name__ == "__main__":
#     main()