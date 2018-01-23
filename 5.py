#Ask the temperature from te user and print :
#if T less then <32 wear jacket
# if < less than 10 wear boots
# if more than >70 wear t-shirt
#if less than <70 wear pans


temp = int(input("What is the temperature?:"))
if temp <10:
    print("Please wear the boots, son")
elif temp <32:
    print("Please wear the jacket")
elif temp <70:
    print("Please wear your pans, son")
elif temp >70:
    print("Wear your t-shirt")
else:
    print("Please enter a valid number ")