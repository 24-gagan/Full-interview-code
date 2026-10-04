import requests

print("status code check")
response = requests.get("https://api.github.com/user")
if response.status_code == 200:
    print(response.status_code)
    print(response.json())
else:
    print(response.status_code)
