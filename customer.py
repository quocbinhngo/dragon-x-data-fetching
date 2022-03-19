import json
import random
import requests

# FETCH USER DATA
# ENDPOINT_URL = "https://api.namefake.com/"
#
# name_set = set()
# customers = []
#
# for i in range(1, 1000):
#     response = requests.get(ENDPOINT_URL)
#     data = response.json()
#
#     name = data["name"]
#     address = data["address"]
#     username = data["username"]
#     password = data["password"]
#     phone = data["phone_w"]
#     company = data["company"]
#     customer_id = data["uuid"]
#
#     if name in name_set:
#         continue
#
#     customer = {"NAME": name,
#                 "ADDRESS": address,
#                 "USERNAME": username,
#                 "PASSWORD": password,
#                 "PHONE": phone,
#                 "COMPANY": company,
#                 "CUSTOMER_ID": customer_id}
#     customers.append(customer)
#
# with open("./json/customer_data.json", "w") as file:
#     json_obj = json.dumps(customers, indent=4)
#     file.write(json_obj)
#
# print(len(customers))

# MODIFY DATA

# get customer and country
with open("./json/customer_data.json", "r") as file:
    customer_data = json.load(file)

with open("./json/country_data.json", "r") as file:
    country_data = json.load(file)




