import requests

print("API first request")
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print(response.json())
print()
