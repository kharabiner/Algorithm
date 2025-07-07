import sys

N = int(sys.stdin.readline())

myset = {N}
cnt = 0
while 1 not in myset:
  tmp = set()
  for i in myset:
    if i%3 == 0:
      tmp.add(i//3)
    if i%2 == 0:
      tmp.add(i//2)
    if N != 1:
      tmp.add(i-1)
  myset = tmp
  cnt += 1
  
  
print(cnt)