import random
import requests
import json

from random_date import random_date

ENDPOINT_URL = "https://api.spacexdata.com/v4/launches"

# Request data from SpaceX API
response = requests.get(ENDPOINT_URL)
data = response.json()

# Get the launch's info
launches = []


for launch in data:
    img_url = launch["links"]["patch"]["small"]
    launch_date = launch["static_fire_date_utc"]
    success = launch["success"]
    name = launch["name"]
    launch_id = launch["id"]
    rocket_id = random.randint(1, 40)

    if launch_date is None:
        launch_date = random_date()
    else:
        day_time = launch_date.split('T')
        launch_date = " ".join([day_time[0], day_time[1][:8]])

    launch_data = {"IMG_URL": img_url,
                   "LAUNCH_DATE": launch_date,
                   "SUCCESS": launch["success"],
                   "NAME": launch["name"],
                   "LAUNCH_ID": launch["id"],
                   "ROCKET_ID": random.randint(1, 40)}

    launches.append(launch_data)

with open("./json/launch_data.json", "w") as file:
    json_obj = json.dumps(launches, indent=4)
    file.write(json_obj)

print(len(launches))