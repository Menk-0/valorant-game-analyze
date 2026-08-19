import json
with open("my_matches.json",'r') as file:
    loader=json.load(file)
needed_matches=[]
for matches in loader["data"]:
      if matches["metadata"]["mode"]=="Competitive":
           needed_matches.append(matches)
with open("compe.json",'w') as file:
     json.dump(needed_matches, file,indent=4)