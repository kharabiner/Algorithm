import sys

input = sys.stdin.readline

n = int(input())
current = 0
for _ in range(n):
  code = input().strip()
  if code.count('for')+code.count('while') > current:
    current = code.count('for')+code.count('while')

print(current)