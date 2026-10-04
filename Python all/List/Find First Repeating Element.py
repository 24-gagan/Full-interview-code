lst = [10, 5, 3, 4, 3, 5, 6]
seen = set()

for i in lst:
    if i in seen:
        print("First repeating:", i)
        break
    seen.add(i)
