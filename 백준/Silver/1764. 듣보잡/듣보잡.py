import sys

N, M = map(int, sys.stdin.readline().split())

hnames = set()
for _ in range(N):
  hname = sys.stdin.readline().strip()
  hnames.add(hname)

snames = set()
for _ in range(M):
  sname = sys.stdin.readline().strip()
  snames.add(sname)

hsnames = sorted(hnames & snames)

print(len(hsnames))
for hsname in hsnames:
  print(hsname)