from collections import deque

T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  documents = deque(map(int, input().split()))

  cnt = 0
  while documents:
    if max(documents) == documents[0]:
      if M == 0:
        print(cnt+1)
        break
      documents.popleft()
      cnt += 1
      M -= 1
      if M < 0:
        M = len(documents)-1
    else:
      documents.append(documents.popleft())
      M -= 1
      if M < 0:
        M = len(documents)-1
      
