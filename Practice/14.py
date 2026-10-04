str1 = "/*Jon is @developer & musician"

str2="".join(ch for ch in str1 if ch.isalnum())
print(str2)