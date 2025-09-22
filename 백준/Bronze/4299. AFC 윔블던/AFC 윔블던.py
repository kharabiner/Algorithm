import sys
input = sys.stdin.readline

s, d = map(int, input().split())

a = (s+d)/2
b = s - a

if s < d or (s + d) % 2 != 0:
    print(-1)
else:
    a = (s + d) // 2
    b = (s - d) // 2
    
    print(a, b)
