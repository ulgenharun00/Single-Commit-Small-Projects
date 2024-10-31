import requests
from datetime import datetime as dt

USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph1"
today_date = dt.now().strftime("%Y%m%d")
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixel_data = {
    "date": today_date,
    "quantity": "21.53",
}

new_pixel_data = {
    "quantity": ""
}

response = requests.put(url=put_pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)