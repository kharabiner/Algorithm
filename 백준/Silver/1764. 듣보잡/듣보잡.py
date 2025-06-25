import sys
input = sys.stdin.readline

# 입력: 듣도 못한 사람 수 N, 보도 못한 사람 수 M
N, M = map(int, input().split())

# 듣도 못한 사람 명단을 set으로 저장
heard = {input().strip() for _ in range(N)}

# 듣보잡 명단: 보도 못한 사람 중 듣도 못한 사람과 겹치는 이름
result = []
for _ in range(M):
    name = input().strip()
    if name in heard:
        result.append(name)

# 사전순 정렬 후 출력
result.sort()
print(len(result))
print(*result, sep='\n')