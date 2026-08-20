import requests
import json
import os
import sys
from dotenv import load_dotenv
load_dotenv()
key=os.getenv("apikey")

name_withoutnametag=input("Enter name witout tagline- ") #taking the name in without the tagline

#checking if the name is valid via the naming length convention

if len(name_withoutnametag)>=3 and len(name_withoutnametag)<=16:
    pass
else:
    print("enter a valid name")
    quit()
taglineonly=input("Enter your tagline the #- ") #tagline taking

#checking if the tagline is valid via the length convention

if len(taglineonly)>=3 and len(taglineonly)<=5:
    pass
else:
    print("Please enter a valid tagline")
    quit()

#taking region of player
region_of_player=input("Enter your region only in the format of na, eu, ap, kr- ").lower()

validregion=["kr","ap","na", "eu"] #to check if picking the right region or not

if (region_of_player not in validregion):
    print("Enter a valid region")
    quit()

url=f"https://api.henrikdev.xyz/valorant/v3/matches/{region_of_player}/{name_withoutnametag}/{taglineonly}"

wallet={"Authorization":key}

response=requests.get(url,headers=wallet)

if response.status_code == 200:
    match_data = response.json()
    with open('my_matches.json', 'w') as file:
        json.dump(match_data, file, indent=4)
else:
    print(f"Failed to connect, Error code: {response.status_code}")