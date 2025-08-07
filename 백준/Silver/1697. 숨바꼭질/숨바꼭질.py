from collections import deque

N, K = map(int, input().split())

MAX_POS = 100000
visited = [-1] * (MAX_POS + 1)

def bfs(n, k):
  q = deque()
  q.append(n)
  visited[n]=0
  while q:
    current = q.popleft()
    
    if current == k:
      print(visited[current])
      return

    for next in (current-1, current+1, current*2):
      if 0 <= next <= MAX_POS and visited[next] == -1:
        visited[next] = visited[current]+1
        q.append(next)

bfs(N, K)