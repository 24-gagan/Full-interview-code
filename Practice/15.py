str1 = 'I am 25 years and 10 months old'

str2="".join(ch for ch in str1 if ch.isdigit())
print(str2)