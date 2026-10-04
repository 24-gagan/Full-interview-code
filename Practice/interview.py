d = {"a": 3, "b": 1, "c": 2}
dict1 = dict(sorted(d.items(), key=lambda x: x[1]))
print(dict1)
