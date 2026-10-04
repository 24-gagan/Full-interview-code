s = "aabbccdde"
res = ""

for ch in s:
    if not res or ch != res[-1]:
        res += ch

print(res)
