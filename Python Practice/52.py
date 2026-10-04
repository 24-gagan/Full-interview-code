from collections import Counter
text="Hello world hello"
words=text.lower().split()
word_count=Counter(words)
print(word_count)