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
        return result
    return False

is_playing = False
last_status_change_time = 0

while True:
    new_status = request_status()

    if new_status != is_playing:
        last_status_change_time = time.time()

    if new_status and not is_playing:
        is_playing = True
        # Start Amp here
        print("Amp started")
    elif not new_status and is_playing:
        # Wait for 10 mins before stopping amp if nothing changes
        time_since_change = time.time() - last_status_change_time
        if time_since_change >= 600:  # 10 minutes = 600 seconds
            is_playing = False
            # Stop Amp here (Replace this comment with the actual code to stop the Amp)
            print("Amp stopped.")
        else:
            print(f"Status unchanged. {time.time()} {last_status_change_time} {time_since_change} Waiting for {600 - int(time_since_change)} seconds before stopping Amp.")

    elif new_status and is_playing:
        # If the status remains unchanged but is currently playing
        print("Status unchanged. Amp is already playing.")


    time.sleep(3)