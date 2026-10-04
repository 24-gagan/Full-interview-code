person={"name":"Alice","age":28}
city=person.get("city","unknown")
print(city)
if "city" in person:
    print(person["city"])
else:
    print("City not found")
try:
    print(person["city"])
except KeyError:
    print("Key city doesnot exist")