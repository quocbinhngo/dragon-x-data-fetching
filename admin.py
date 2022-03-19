import requests
import string
from random_password import random_password

ENDPOINT_URL = "https://jsonplaceholder.typicode.com/users"

response = requests.get(ENDPOINT_URL)
data = response.json()
admin_data = []


for admin in data:
    admin_id = admin["id"]
    name = admin["name"]
    email = admin["email"]
    address = ", ".join([admin["address"]["street"], admin["address"]["suite"], admin["address"]["city"]])
    password = random_password()

    admin_data.append({"ADMIN_ID": admin_id,
                       "NAME": name,
                       "EMAIL": email,
                       "PASSWORD": password})

