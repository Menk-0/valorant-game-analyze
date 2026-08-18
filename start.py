name_withoutnametag=input("Enter name witout tagline- ")
if len(name_withoutnametag)>=3 and len(name_withoutnametag)<=16:
    pass
else:
    print("enter a valid name")
    quit()
taglineonly=input("Enter your tagline the #- ")
if len(taglineonly)>=3 and len(taglineonly)<=5:
    pass
else:
    print("Please enter a valid tagline")
    quit()
region_of_player=input("Enter your region only in the format of na, eu, ap, kr- ").lower()
validregion=["kr","ap","na", "eu"]
if (region_of_player not in validregion):
    print("Enter a valid region")
    quit()