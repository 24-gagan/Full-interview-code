import requests

print("Status Code check")
response = requests.get("http://api.open-notify.org/astros.json")
if response.status_code == 200:
    print(response.status_code)
else:
    print(response.status_code)
print()
