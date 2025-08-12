import sys
input = sys.stdin.readline

length = int(input())
string = input().strip()

s, n = (1,0) if string[0]=='S' else (0,1)
prev = string[0]
magnet_max = 0
for ch in string[1:]:
  
  if prev == ch == 'S':
    s += 1
  elif prev == ch == 'N':
    n += 1
  elif prev != ch == 'S':
    s = 1
  else:
    n = 1

  magnet_max = max(magnet_max, min(s,n)*2)

  prev = ch

print(magnet_max)
  
  