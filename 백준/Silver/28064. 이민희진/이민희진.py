n = int(input())
names = [input().strip() for _ in range(n)]

def match(name1, name2):
  n = min(len(name1), len(name2))
  for i in range(1, n+1):
    #print(name1[len(name1)-i:], name2[:i])
    #print(name2[len(name2)-i:], name1[:i])
    if name1[len(name1)-i:]==name2[:i] or name2[len(name2)-i:]==name1[:i]:
      #print('find#####################')
      return True
  return False

cnt = 0
for i in range(n-1):
  for j in range(i+1, n):
    if match(names[i], names[j]):
      cnt += 1

print(cnt)
    