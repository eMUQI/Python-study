favorite_numbers = {"Andy": [1, 2], "Candy": 2,
                    "Jack": [13, 15], "Mark": 6, "Mary": 7}
for temp in favorite_numbers.keys():
    if(type(favorite_numbers[temp]) == type(1)):
        print(temp.title()+"'s favorite_number is " +
              str(favorite_numbers[temp]))
    else:
        print(temp.title()+"'s favorite_number are " +
              str(favorite_numbers[temp])[1:-1])
