import requests
from urllib.parse import urlencode
import settings 

def get_summoner_info(summoner_name=None, region=settings.DEFAULT_REGION_CODE):
    #gets info about summoner
    params = {
            'api_key': settings.API_KEY
        }
    if not summoner_name:
        summoner_name = input("Summoner name: ")
        
    api_url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    # https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/adhrin?api_key=...

    try:
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print("abc")
        print(f'Issue getting summoner info from API: {err}')
        return None

def get_match_ids_by_summoner_puuid(summoner_puuid, matches_count, region=settings.DEFAULT_REGION):
    params = {
        'api_key': settings.API_KEY,
        'count': matches_count,
    }
    api_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{summoner_puuid}/ids"
    try:
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f'Issue getting summoner match data from API: {err}')
        return None

def did_player_win_match(summoner_puuid, match_id, region=settings.DEFAULT_REGION):
    params = {
        'api_key': settings.API_KEY,
    }
    api_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}"

    try:
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        match_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f'Issue getting match data from match id from API: {e}')
        return None

    if summoner_puuid in match_data['metadata']['participants']:
        player_index = match_data['metadata']['participants'].index(summoner_puuid)
    else:
        return None

    player_info = match_data['info']['participants'][player_index]
    return player_info['win']

        
        
        



