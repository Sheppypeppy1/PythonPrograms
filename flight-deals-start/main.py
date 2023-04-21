import requests
from pprint import pprint

sheety_api = "https://api.sheety.co/781b5b90b4f9ac70b058bd1dda66916d/flightDeals/prices"

response = requests.get(sheety_api)
data = response.json()
sheet_data = data["prices"]
pprint(sheet_data)

for item in sheet_data:
    if item["iataCode"]=="":
        item["iataCode"]="Testing"
