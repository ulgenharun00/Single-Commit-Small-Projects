from datetime import datetime
import requests, os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
EXERCISE_ENDPOINT = os.environ["EXERCISE_ENDPOINT"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
TOKEN = os.environ["TOKEN"]

text = str(input("Tell me which exercises you did: "))

parameters = {
    "query": text,
    "gender": "male",
    "weight_kg": 85,
    "height_cm": 183,
    "age": 19,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
    }


    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)