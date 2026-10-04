str_="geeksforgeeks"
str1=("gfo")
str2="abc"
mapped=str.maketrans(str1,str2)
print(str_)
print(str_.translate(mapped))