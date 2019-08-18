import string

favorite_fruits = ["fruit"+i for i in string.ascii_uppercase[:3]]
print(favorite_fruits)

if "fruitA" in favorite_fruits:
    print("You really like fruitA!")
if "fruitB" in favorite_fruits:
    print("You really like fruitB!")
if "fruitC" in favorite_fruits:
    print("You really like fruitC!")
if "fruitD" in favorite_fruits:
    print("You really like fruitD!")
if "fruitE" in favorite_fruits:
    print("You really like fruitE!")
