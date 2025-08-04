import sys
import string
word = sys.stdin.readline()

for letter in string.ascii_lowercase:
  print(word.find(letter), end=' ')