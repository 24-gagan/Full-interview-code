my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
del my_dict["profession"]
if "age" in my_dict:
    print("key is present with",my_dict["age"])
else:
    print("key not found")