import sys

plain_text = sys.stdin.readline().rstrip()
key = sys.stdin.readline().rstrip()

encrypted_text = ""

for i in range(len(plain_text)):
  plain_char = plain_text[i]
  
  if plain_char == ' ':
      encrypted_text += ' '
      continue
  
  current_key_char = key[i % len(key)]
  
  plain_num = ord(plain_char) - ord('a')
  key_num = ord(current_key_char) - ord('a')
  
  encrypted_num = (plain_num - key_num - 1) % 26
  
  encrypted_text += chr(encrypted_num + ord('a'))

print(encrypted_text)