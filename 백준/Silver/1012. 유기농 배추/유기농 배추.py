import sys
from collections import deque
input = sys.stdin.readline

def bfs(image, x, y, visited, rows, cols):
    queue = deque([(x, y)])
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_clusters(image, rows, cols):
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if image[i][j] == 1 and not visited[i][j]:
                bfs(image, i, j, visited, rows, cols)
                count += 1
    return count

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    binary_image = [[0] * N for _ in range(M)]
    for _ in range(K):
        X, Y = map(int, input().split())
        binary_image[X][Y] = 1
    print(count_clusters(binary_image, M, N))