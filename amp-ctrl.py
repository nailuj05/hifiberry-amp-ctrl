import requests
x = requests.get("http://127.0.0.1:81/api/player/status")

if x.status_code == '200':
    print(x.content)
