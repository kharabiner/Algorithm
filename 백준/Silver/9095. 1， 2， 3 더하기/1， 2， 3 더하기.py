import sys
T = int(sys.stdin.readline())

arr = [1, 1, 2, 4, 7]
for i in range(5, 12):
  arr.append(arr[i-1] + arr[i-2] + arr[i-3])
  
for _ in range(T):
  n = int(sys.stdin.readline())
  print(arr[n])