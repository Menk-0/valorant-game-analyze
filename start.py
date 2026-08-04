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