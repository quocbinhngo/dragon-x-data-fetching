import random
import json

# Random name for choosing
ROCKET_NAME = ["Face", "Blue", "Sky", "Earth", "Sun", "Moon", "Planet",
               "Five", "Green", "Falcon", "Evil", "Origin", "Vina", "Gema"]

MANUFACTURER_NAME = ["SPACEX", "LEOLABS", "GHGSAT", "ORBITAL INSIGHT",
                     "SLINGSHOT AEROSPACE", "ROCKET LAB", "PLANET", "RELATIVITY SPACE",
                     "Blue Origin", "Virgin Galactic", "Bigelow Aerospace",
                     "Lockheed Martin, Boeing and United Launch Alliance"]

rockets = []
name_list = set()


for i in range(1, 41):
    while True:

        # Get rocket name
        word1 = random.choice(ROCKET_NAME)
        word2 = random.choice(ROCKET_NAME)
        rocket_name = word1 + " " + word2

        # Other info
        rocket_id = i
        manufacturer = random.choice(MANUFACTURER_NAME)

        if word1 != word2 and rocket_name not in name_list:
            rocket = {"NAME": rocket_name,
                      "ROCKET_ID": rocket_id,
                      "MANUFACTURER": manufacturer}
            rockets.append(rocket)
            name_list.add(rocket_name)
            break

rockets = list(rockets)

with open("./json/rocket_data.json", "w") as file:
    json_obj = json.dumps(rockets, indent=4)
    file.write(json_obj)
