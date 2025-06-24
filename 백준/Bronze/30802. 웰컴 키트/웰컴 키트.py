import sys

N = int(sys.stdin.readline())
size = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

# 첫 줄에 티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지 출력
cnt=0
for i in size:
  cnt += i//T
  if i%T != 0:
    cnt += 1

print(cnt)

# 다음 줄에 펜을 P자루씩 최대 몇 묶음 주문할 수 있는지와, 그 때 펜을 한 자루씩 몇 개 주문하는지 구하기
print(sum(size)//P, sum(size)%P)