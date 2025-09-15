import sys
input = sys.stdin.readline

X = int(input().strip())

string = str(X)

def plus(string):
  sum = 0
  for i in string:
    sum += int(i)
  return str(sum)

cnt = 0
while len(string) > 1:
  string = plus(string)
  cnt += 1

print(cnt)
if int(string) in (3,6,9):
  print('YES')
else:
  print('NO')
