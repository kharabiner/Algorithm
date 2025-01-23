import sys

input = sys.stdin.readline
# 명령의 수 N 입력 받기
N = int(input())

# 스택으로 사용할 리스트
stack = []

# N개의 명령 입력 받아 실행하는 로직
for _ in range(N):
    order = input().split()
    if order[0] == "push":
        stack.append(order[1])
    elif order[0] == "pop":
        print(stack.pop() if len(stack) != 0 else -1)
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    elif order[0] == "top":
        print(stack[len(stack) - 1] if len(stack) != 0 else -1)
