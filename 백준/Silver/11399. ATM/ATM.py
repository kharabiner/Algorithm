N = int(input())
Pi = sorted(list(map(int, input().split())))
for i in range(N-1):
  Pi[i+1] += Pi[i]
print(sum(Pi))