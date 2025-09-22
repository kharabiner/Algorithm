import sys
input = sys.stdin.readline

input_string = input().strip().split('-')
for s in input_string:
  print(s[0], end='')