import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  H, W, N = map(int, input().split())
  floor = N % H if N % H != 0 else H
  room = N // H if N % H == 0 else N // H + 1
  print(floor * 100 + room)