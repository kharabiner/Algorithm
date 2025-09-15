import sys

input = sys.stdin.readline

N = int(input())
numbers = []
for n in range(N):
  n = int(input())
  numbers.append(n)
  
numbers.sort()

for n in numbers:
  print(n)