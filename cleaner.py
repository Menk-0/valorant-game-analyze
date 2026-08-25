import json
import os

with open("my_matches.json",'r') as file:
    loader=json.load(file)
needed_matches=[]

def unrated():
     if not os.path.exist("unrated.json"):
          for matches in loader["data"]:
               if matches["metadata"]["mode"]=="Unrated":
                    needed_matches.append(matches)
          with open("unrated.json",'w') as file:
               json.dump(needed_matches, file,indent=4)
          print("\nunrated data json is created\n")
     else:
          print("\nPath already exists moving on\n")

def deathmatch():
     if not os.path.exists("deathmatch.json"):
          for matches in loader["data"]:
               if matches["metadata"]["mode"]=="Deathmatch":
                    needed_matches.append(matches)
          with open("deathmatch.json",'w') as file:
               json.dump(needed_matches, file,indent=4)
          print("\ndeathmatch data json is created\n")
     else:
          print("\nPath already exists moving on\n")

def competitive():
     if not os.path.exists("competitive.json"):
          for matches in loader["data"]:
               if matches["metadata"]["mode"]=="Competitive":
                    needed_matches.append(matches)
          with open("competitive.json",'w') as file:
               json.dump(needed_matches, file,indent=4)
          print("\ncompetitive data json is created\n")
     else:
          print("\nPath already exist moving on\n")

def others():
     if not os.path.exists("others.json"):
          for matches in loader["data"]:
               if matches["metadata"]["mode"] not in ["Competitive","Unrated","Deathmatch"]:
                    needed_matches.append(matches)
          with open("others.json","w") as file:
               json.dump(needed_matches,file,indent=4)
          print("\nData for other's mode is created\n")
     else:
          print("\npath already exists moving on\n")