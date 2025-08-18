import sys
input = sys.stdin.readline

N = int(input())

if N == 0:
  print("NO")
  exit()

factorials = [1] * 21
for i in range(1, 21):
  factorials[i] = factorials[i-1] * i

for i in range(20, -1, -1):
  if N >= factorials[i]:
    N -= factorials[i]
        
  if N <= 0:
    break

if N == 0:
  print("YES")
else:
  print("NO")