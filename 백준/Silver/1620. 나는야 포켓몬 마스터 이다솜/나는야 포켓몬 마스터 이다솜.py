import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon_dict = {}
pokemon_list = []

for i in range(1, N+1):
    pokemon_name = input().rstrip()
    pokemon_dict[pokemon_name] = i
    pokemon_list.append(pokemon_name)

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(pokemon_list[int(question)-1])
    else:
        print(pokemon_dict[question])