from helper import get_summoner_info, get_match_ids_by_summoner_puuid, did_player_win_match
summoner_name = "adhrin"

summoner = get_summoner_info(summoner_name)
print(summoner)
print(summoner['name'])

matches = 20
summoner_match_ids = get_match_ids_by_summoner_puuid(summoner['puuid'], matches)
print(summoner_match_ids)

n = 0
wins = 0
while n<20:
    win = did_player_win_match(summoner['puuid'],summoner_match_ids[n])
    if(win == True):
        wins+=1
    n+=1

pct = wins/matches

print(f"This summoners win percentage was {pct}")