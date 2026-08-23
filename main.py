#run this only
import os
import json

checkregion=["kr","ap","na","eu"]

if not os.path.exists("user.json"):
    
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

    with open("user.json", "w") as file:
        json.dump(user_data,file,indent=4)
    import config
else:
    print("User already exist if want to re enter identity delete user.json moving onto fetching")

if not os.path.exist("my_matches.json"):
    import fethcher
else:
    print("Data for user already exist moving onto cleaner")
