import sys

fibonacci = [1, 0, 1]
for i in range(3, 42):
  fibonacci.append(fibonacci[i-2] + fibonacci[i-1])

T = int(sys.stdin.readline())
for _ in range(T):
  N = int(sys.stdin.readline())
  print(fibonacci[N], fibonacci[N+1]) 
  