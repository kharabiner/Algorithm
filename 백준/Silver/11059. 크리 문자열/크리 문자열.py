import sys
input = sys.stdin.readline

S = input().rstrip()
S_len = len(S)

def 크리(string):
  length = len(string)
  if length == 0 or length % 2 != 0:
    return False

  front = 0
  for i in string[:length//2]:
    front += int(i)
  back = 0
  for i in string[length//2:]:
    back += int(i)
  
  if front == back:
    return True
  else:
    return False
'''
길이 = 0
for first in range(S_len):
  for last in range(first+2, S_len+1, 2):
    print('확인', first, last)
    if 크리(S[first:last]) and 길이 < last-first:
      길이 = last-first

print(길이)
'''
max_len = S_len if S_len % 2 == 0 else S_len - 1

for length in range(max_len, 0, -2):
  for start in range(S_len - length + 1):
    substring = S[start : start + length]
    if 크리(substring):
      print(length)
      sys.exit(0)