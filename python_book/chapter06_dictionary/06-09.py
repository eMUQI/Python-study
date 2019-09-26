favorite_places = {"Jack": ["Beijing", "Paris"],
                   "Mark": "Shanghai",
                   "Mary": ["Guangzhou", "Princeton"],
                   }
for name, place in favorite_places.items():
    print(name + " love "+str(place)[1:-1])
