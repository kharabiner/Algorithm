nums = list(map(int, input().split()))
nums = [i**2 for i in nums]
print(sum(nums) % 10)
