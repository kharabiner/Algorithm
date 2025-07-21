import math
n = int(input())
n_factorial = math.factorial(n)
count = 0
while True:
  if n_factorial % 10 == 0:
    count += 1
    n_factorial //= 10
  else:
    break

print(count)