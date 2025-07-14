import sys
input = sys.stdin.readline

n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 끝나는 시간을 기준으로 정렬 (끝나는 시간이 같으면 시작시간 기준)
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

for start, end in meetings:
    # 현재 회의의 시작시간이 이전 회의 끝나는 시간보다 크거나 같으면 선택
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)