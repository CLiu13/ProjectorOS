raw=input("Please enter a percentage here (Omit %): ")
percent=int(raw)
if percent >= 100:
    print("\n")    
    print("Please enter a percentage less than 100%")
else:
    print("\n")
    print("You entered", percent, "%")
