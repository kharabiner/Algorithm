import sys

input = sys.stdin.readline

N = int(input())
num = [int(input()) for _ in range(N)]

sorted_num = sorted(num)

[print(x) for x in sorted_num]
