import sys

input = sys.stdin.readline

N = int(input())

members = [
    (int(age), name, index)
    for age, name, index in [[*input().split(), i] for i in range(N)]
]

members.sort(key=lambda x: (x[0], x[2]))

for i in range(N):
    print(members[i][0], members[i][1])
