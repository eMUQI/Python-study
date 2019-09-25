active = True
while active:
    str = input("How old are you ? ")
    if str == "quit":
        break
    age = int(str)
    if age < 3:
        print("free")
    elif age < 13:
        print("$5")
    else:
        print("$15")
