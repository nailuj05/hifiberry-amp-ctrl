import requests
x = requests.get("http://127.0.0.1:81/api/player/status")

print(x.status_code)
print(x)
