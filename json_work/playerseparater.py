import os
import json
import sys
sys.path.append("..")
from config import NAME,TAG

#separate the matches from my matches and analyze them in the category of each mode but for player only
with open("json_files/my_matches.json",'r') as file:
    loader=json.load(file)

needed_matches=[]

if not os.path.exists("json_files/playerseparated.json"):
    for matches in loader["data"]:
        metadata=matches.get("metadata")
        all10playerdata=matches["players"]["all_players"]
        for data in all10playerdata:
            if data["name"]==NAME and data["tag"]==TAG:
                needed_matches.append(data)
    returning={
        "metadata": metadata,
        "players": {
            "all_players": needed_matches
        }
    }
    with open("json_files/playerseparated.json",'w') as file:
        json.dump(returning, file,indent=4)
    print("\n spearate player data json is created\n")
else:
    print("\n separate player data already exists moving on\n")

needed_matches=[]

if not os.path.exists("json_files/otherplayerseparated.json"):
    for matches in loader["data"]:
        metadata=matches.get("metadata")
        all10playerdata=matches["players"]["all_players"]
        for data in all10playerdata:
            if data["name"]!=NAME and data["tag"]!=TAG:
                needed_matches.append(data)
    returning={
        "metadata": metadata,
        "players": {
            "all_players": needed_matches
        }
    }
    with open("json_files/otherplayerseparated.json",'w') as file:
        json.dump(returning, file,indent=4)
    print("\n other spearate player data json is created\n")
else:
    print("\n other separate player data already exists moving on\n")