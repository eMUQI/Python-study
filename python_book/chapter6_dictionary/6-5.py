Rivers = {"RiverA": "CountryA", "RiverB": "CountryB", "RiverC": "CountryC"}
for key, value in Rivers.items():
    print("The %s runs through %s." % (key, value))

for key in Rivers.keys():
    print(key)
print()
for value in Rivers.values():
    print(value)
