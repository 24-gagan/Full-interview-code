data = {"a": 10, "b": 25, "c": 15}
dict1 = min(data, key=data.get)  # key ki value lekar compare karo
print(dict1)
