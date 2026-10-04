str1 = "testing concepts"

result = ""

for i, ch in enumerate(str1):
    if ch == 't' and i != 0:
        result += "*"
    else:
        result += ch

# add extra * before last 's'
result = result.replace("*s", "**s")

print(result)
