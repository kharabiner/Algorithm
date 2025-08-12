import sys
input = sys.stdin.readline

N, M = map(int, input().split())
helmet_defense = list(map(int, input().split()))
vest_defense = list(map(int, input().split()))

print(max(helmet_defense)+max(vest_defense))