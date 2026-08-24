import os
import json

NAME=None
TAG=None
REGION=None

if os.path.exists("user.json"):
    with open("user.json") as file:
        data=json.load(file)
        NAME=data["NAME"]
        TAG=data["TAG"]
        REGION=data["REGION"]
        URL=f"https://api.henrikdev.xyz/valorant/v3/matches/{REGION}/{NAME}/{TAG}"
        print("Variable setup is done")

if NAME==None and TAG==None and REGION==None:
    print("run main .py and start over the variables are not setup")
    quit()