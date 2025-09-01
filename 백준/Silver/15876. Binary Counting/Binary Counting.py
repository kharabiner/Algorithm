n, k = map(int, input().split())

lenth = n*5+k
bin_list = ''
num = 0

while len(bin_list) <= lenth:
  bin_num = f'{num:b}'
  bin_list += bin_num
  num += 1


for i in range(5):
  print(bin_list[n*i+k-1], end=' ')