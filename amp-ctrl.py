import requests
import json
import time

def check_players_playing(json_data):
    # Decode the JSON data
    data = json_data
    
    # Get the list of players from the JSON data
    players = data.get('players', [])
    
    # Check if any player is playing
    for player in players:
        if player.get('state') == 'playing':
            return True
    
    return False

def request_status():
    x = requests.get("http://127.0.0.1:81/api/player/status")

    if x.status_code == 200:
        content = x.json()
        result = check_players_playing(content)
        print(result)

while True:
    request_status()
    time.sleep(3)