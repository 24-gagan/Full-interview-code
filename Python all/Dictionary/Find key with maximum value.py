data = {"a": 10, "b": 25, "c": 15}
max_key = max(data, key=data.get)  # get key ki value lekar compare karo
print(max_key)
