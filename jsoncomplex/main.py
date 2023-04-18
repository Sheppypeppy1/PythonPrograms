import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "c792dbba812b200d8df64451c73d4d10"
account_sid = "AC5d6f47111abd9b00b0db916cc9a766eb"
auth_token = "fe9121c5f85892d9b5c08adca10b6eb7"

weather_params = {
    "lat":51.4584,
    "lon":0.1891,
    "appid":api_key
}

def get_json():
    response = requests.get(OWM_endpoint, params=weather_params)
    response.raise_for_status()
    return response.json()

def rain_today():
    weather_data = get_json()
    weather_list = weather_data["list"]
    daily_weather = weather_list[:4]

    id_list = [item["weather"][0]["id"] for item in daily_weather]
    print(id_list)
    smallest_id = min(id_list)
    if smallest_id < 700:
        return True
    else:
        return False

if rain_today():
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        from_="+14454553767",
        body="Its going to rain in Wandsworth today Mitchel. Bring an umbrella! ☔️",
        to="+447464789801"
    )

    print(message.status)
    