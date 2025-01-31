from collections import deque

N, K = map(int, input().split())

nums = deque(range(1,N+1))
used_nums = []

while(nums):
    for _ in range(K):
        n = nums.popleft()
        nums.append(n)
    used_nums.append(nums.pop())

print(str([x for x in used_nums]).replace('[', '<').replace(']', '>'))