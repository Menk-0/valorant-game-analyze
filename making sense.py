import json
with open("matches.json") as file:
    loader=json.load(file)
playername=input("player name without tag")
if len(playername)>=3 and len(playername)<=16:
    pass
else:
    print("enter a valid name")
    quit()
playertag=input("player tag only")
if len(playertag)>=3 and len(playertag)<=5:
    pass
else:
    print("Please enter a valid tagline")
    quit()
myplayerdata=[]
for matches in loader["data"]["metadata"]:
    print(matches["all_players"]["name"])