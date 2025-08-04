test_cases = int(input())

for _ in range(test_cases):
  string = input().rstrip()
  
  score = 0
  current = 0
  for s in string:
    if s == "O":
      current += 1
      score += current
    else:
      current = 0
  print(score)