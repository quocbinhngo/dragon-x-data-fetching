import requests
import json

ENDPOINT_URL = "https://restcountries.com/v2/all"

response = requests.get(ENDPOINT_URL)
data = response.json()
country_list = []

for country in data:
    country_list.append({"NAME": country["name"],
                         "REGION": country["region"]})

with open("./json/country_data.json", "w") as file:
    json_obj = json.dumps(country_list, indent=4)
    file.write(json_obj)

print(len(country_list))

