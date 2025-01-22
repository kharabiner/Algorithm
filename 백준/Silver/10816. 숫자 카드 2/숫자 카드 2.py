import sys

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))

# 카드 숫자 세기를 한 번만 수행
count_dict = {}
for card in cards:
    count_dict[card] = count_dict.get(card, 0) + 1

# 검색할 숫자들 확인
print(*[count_dict.get(x, 0) for x in checks])
