sandwich = ["sandwichA", "pastrami",
                   'sandwichB', "pastrami", 'sandwichC', "pastrami"]
print("pastrami are sold out")
while "pastrami" in sandwich:
    sandwich.remove("pastrami")
print("we have "+str(sandwich))