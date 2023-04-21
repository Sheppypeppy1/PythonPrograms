import requests
from requests.auth import HTTPBasicAuth
from datetime import date, datetime

GENDER = "Male"
WEIGHT_KG = 84
HEIGHT_CM = 183
AGE = 25

TOKEN = "Basic c2hlcHB5cGVwcHk6REVCb3JhaDAwMTg="
APP_ID = "5d77a191"
API_KEY = "c5f5132f2449640f0346c7c9d73db9e9"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
add_row_endpoint = "https://api.sheety.co/781b5b90b4f9ac70b058bd1dda66916d/myWorkouts/workouts"

exercise_text= input("Tell me which exercises you did: ")

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}

parameters = {
    "query" : exercise_text,
    "gender" : GENDER,
    "height_cm" : HEIGHT_CM,
    "weight_kg" : WEIGHT_KG,
    "age" : AGE
}

response = requests.post(exercise_endpoint,json=parameters,headers=headers)
result = response.json()

today = date.today()
time = datetime.now()
current_time = time.strftime("%H:%M:%S")

parameters2 = {
    "workout":{
        "date":str(today),
        "time":current_time,
        "exercise":result["exercises"][0]["user_input"],
        "duration":result["exercises"][0]["duration_min"],
        "calories":result["exercises"][0]["nf_calories"]
    }
}

headers2 = {
    "Authorization":TOKEN
}

response = requests.post(add_row_endpoint, json=parameters2, headers=headers2)
result = response.json()
print(result)

