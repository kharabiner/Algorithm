import sys

input = sys.stdin.readline

N = int(input())
coordinates = [list(map(int, input().split())) for _ in range(N)]

sorted_coordinates = sorted(coordinates, key=lambda x: (x[0], x[1]))

for sorted_coordinate in sorted_coordinates:
    print(*sorted_coordinate)
