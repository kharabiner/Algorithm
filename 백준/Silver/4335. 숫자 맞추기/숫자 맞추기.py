import sys
input = sys.stdin.readline

high = []
low = []

while True:
  num = int(input().strip())
  if num == 0:
    break
  guess = input().strip()
  if guess == 'too high':
    high.append(num)
  elif guess == 'too low':
    low.append(num)
  else:
    is_honest = True
    for g in high:
      if g <= num:
        is_honest = False
    for g in low:
      if g >= num:
        is_honest = False
        
    if is_honest:
      print('Stan may be honest')
    else:
      print('Stan is dishonest')
    high = []
    low = []

  