d = {"a": 1, "b": 2, "c": 1, "d": 3}
result = {}
seen = set()
for k, v in d.items():
    result[k] = v
    seen.add(v)
print(result)
