#run this only
import os
import json

checkregion=["kr","ap","na","eu"]
if not os.path.exists("json_files"):
    os.makedirs("json_files")

if not os.path.exists("json_files/user.json"):
    
    namein=input("Enter name without tag- ")
    if len(namein)>=3 and len(namein)<=16:
        pass
    else:
        print("enter a valid name")
        quit()
    
    tagin=input("Enter your tag- ")
    if len(tagin)>=3 and len(tagin)<=5:
        pass
    else:
        print("Please enter a valid tagline")
        quit()
    
    regionin=input("Choose your region from kr,ap,na,eu- ")
    if regionin not in checkregion:
        print("Please enter a valid region")
        quit()
    print(f"Creating a directory for user\n name- {namein}\n tag- {tagin}\n region- {regionin}")

    user_data={
    "NAME":namein,
    "TAG":tagin,
    "REGION":regionin
    }

    with open("json_files/user.json", "w") as file:
        json.dump(user_data,file,indent=4)
    import config
else:
    print("\nUser already exist if want to re enter identity delete user.json moving onto fetching\n")

if not os.path.exists("json_files/my_matches.json"):
    import json_work.fethcher as fethcher
else:
    print("Data for user already exist moving onto cleaner\n")

#temporarily in thinking

# import cleaner

# cleanervar=input("Choose what mode to separate or say create a json for with the same spelling\n Unrated\n Competitive \n Deathmatch\n others\n").lower()

# if hasattr(json_work.cleaner, cleanervar):
#     torun=getattr(json_work.cleaner, cleanervar)
#     torun()
#     print(f"Ran {cleanervar} cleaner successfully\n")
# else:
#     print("Enter a valid argument from given")
#     quit()

print("\nCreating separate directories for player and others in player.json and otherplayer.json respectively\n")

import json_work.playerseparater as playerseparater

#import json_work.analyzer as analyzer