n = int(input())
max_price = 0
for _ in range(n):
  a, b, c = map(int, input().split())
  current = 0
  if a == b == c:
    current = 10000+a*1000
  elif a != b != c != a:
    current = max(a,b,c)*100
  else:
    if a == b:
      current = 1000+a*100
    else:
      current = 1000+c*100

  max_price = max(max_price, current)

print(max_price)