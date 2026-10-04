import string

text="Hello,world this is a sample text.Hello world"
words=text.split()
unique_words={word.strip(string.punctuation).lower() for word in words}
print(unique_words)