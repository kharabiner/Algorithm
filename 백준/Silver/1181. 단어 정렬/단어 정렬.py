N = int(input())
words = [input().strip() for _ in range(N)]
words.sort()
words.sort(key=len)

unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)

for word in unique_words:
    print(word)
