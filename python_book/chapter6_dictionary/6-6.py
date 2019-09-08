favorite_language = {
    "jen":"python",
    "sarah":"c",
    "rdward":"ruby",
    "phil":"python",
    }

people_might_take_the_survey = ["lily","jen","sarah","rdward","phil","mike"]

for people in people_might_take_the_survey:
    if people in favorite_language.keys():
        print(people.title()+", thank you for your helping!")
    else:
        print(people.title()+", We need you help!")