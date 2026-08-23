import json

with open("my_matches.json",'r') as file:
    loader=json.load(file)
needed_matches=[]

def unrated():
     for matches in loader["data"]:
      if matches["metadata"]["mode"]=="Unrated":
           needed_matches.append(matches)
     with open("unrated.json",'w') as file:
          json.dump(needed_matches, file,indent=4)
     print("unrated data json is created")

def deathmatch():
     for matches in loader["data"]:
      if matches["metadata"]["mode"]=="Deathmatch":
          needed_matches.append(matches)
     with open("deathmatch.json",'w') as file:
          json.dump(needed_matches, file,indent=4)
     print("deathmatch data json is created")

def competitive():
     for matches in loader["data"]:
      if matches["metadata"]["mode"]=="Competitive":
           needed_matches.append(matches)
     with open("competitive.json",'w') as file:
          json.dump(needed_matches, file,indent=4)
     print("competitive data json is created")