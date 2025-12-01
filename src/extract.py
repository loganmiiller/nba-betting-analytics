import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()

API_KEY = os.getenv("BALLDONTLIE_API_KEY") #API key for balldontlie API
base_url = "https://api.balldontlie.io/v1" #Base URL for balldontlie API

def fetch_teams(): #Fetches NBA teams from the balldontlie API
    url = f"{base_url}/teams"
    headers = {
        "Authorization": API_KEY
    }

    response = requests.get(url, headers=headers)
    
    data = response.json()
    return data["data"]

def fetch_players():
    all_players = []
    cursor = None
    per_page = 100 #maximum allowed by the BallDontLie API
    
    while True:
        params = {'per_page' : per_page}

        if cursor is not None:
            params['cursor'] = cursor

        response = requests.get(
            f"{base_url}/players",
            headers={"Authorization": API_KEY},
            params=params
        )

        print("Status: ", response.status_code)
        
        if response.status_code == 429:
            wait = 5
            print(f"Rate limit. Waiting {wait} seconds.")
            time.sleep(wait)
            continue
        

        data = response.json()
        players = data['data']
        meta = data['meta']

        all_players.extend(players)

        cursor = meta['next_cursor']

        if cursor is None:
            break

        time.sleep(1)

    return all_players

if __name__ == "__main__":
    #teams = fetch_teams()
    players = fetch_players()
    #print(f"Fetched {len(teams)} teams.")
    print(f"Fetched {len(players)} players.")
    #for i in teams:
        #print(i['name'])