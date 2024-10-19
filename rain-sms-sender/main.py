import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""
account_sid = ""
auth_token = ""

# Izmir Location
longitude = 27.092291
latitude = 38.462189
parameters = {
    "lat": latitude,
    "lon": longitude,
    "cnt": 4,
    "appid": api_key
}
response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Today it's going to rain.",
        from_="<SENDER>",
        to="<PHONE NUMBER>"
    )
    print(message.status)