k = int(input())

string = [0, 1]
for i in range(k-1):
  string.append(string[i]+string[i+1])

if k == 1:
  print(0, 1)
else:
  print(string[k-1], string[k])