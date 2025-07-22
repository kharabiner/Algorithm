import sys
input = sys.stdin.readline

num_set = set()
for _ in range(10):
    num = int(input().strip())
    num_set.add(num%42)

print(len(num_set))