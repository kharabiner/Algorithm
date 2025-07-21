n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

for x, y in sorted(points, key=lambda x: (x[1], x[0])):
    print(x, y)