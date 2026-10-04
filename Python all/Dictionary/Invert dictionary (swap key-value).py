d = {"a": 1, "b": 2, "c": 3}  # dictionary
inv = {}  # empty dictionary
for k, v in d.items():  # iterate ove key and value
    inv[v] = k  # value as key and key as value
print(inv)  # print the inv
