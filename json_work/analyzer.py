import json
import os
import pandas as pd

with open("json_files/playerseparated.json") as file:
    my_matches=json.load(file)

with open("json_files/otherplayerseparated.json") as file2:
    other_mathes=json.load(file2)

player=pd.DataFrame(my_matches)

other_players=pd.DataFrame(other_mathes)

print(player)