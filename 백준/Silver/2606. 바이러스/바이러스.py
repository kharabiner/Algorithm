import sys
from collections import defaultdict
n = int(sys.stdin.readline())
edges = int(sys.stdin.readline())

connect = defaultdict(list)

for edge in range(edges):
  f, t = map(int, sys.stdin.readline().split())
  connect[f].append(t)
  connect[t].append(f)

worm = {1}
def add_worm (list):
  if list:
    for i in list:
      if i not in worm:
        worm.add(i)
        add_worm(connect[i])
      
add_worm(connect[1])

print(len(worm)-1)