N = int(input())
A = set(list(map(int, input().split())))

M = int(input())
X = list(map(int, input().split()))

for i in X:
    print(1 if i in A else 0)