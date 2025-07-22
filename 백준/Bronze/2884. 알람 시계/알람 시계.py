import sys
input = sys.stdin.readline

H, M = map(int, input().split())

total = H*60 + M

sol = (total - 45) % 1440

h = sol // 60
m = sol % 60

print(h, m)