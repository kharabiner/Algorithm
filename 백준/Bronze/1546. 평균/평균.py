N = int(input())
scores = list(map(int, input().split()))
M = max(scores)

fix = [i/M*100 for i in scores]
avg = sum(fix)/ len(fix)

print(avg)