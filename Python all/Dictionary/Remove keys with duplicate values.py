d = {"a": 1, "b": 2, "c": 1, "d": 3}
result = {}
seen = set()
for k, v in d.items():
    if v not in seen:
        result[k] = v
        seen.add(v)
print(result)
