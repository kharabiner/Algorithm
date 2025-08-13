from itertools import chain
word = input().strip()
n = len(word)

words = []

for i in range(1, n-1):
  for j in range(i+1, n):
    words.append(''.join(chain(reversed(word[:i]), reversed(word[i:j]), reversed(word[j:]))))
words.sort()
print(words[0])