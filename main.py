import requests
from datetime import datetime

TOKEN = ""

USERNAME = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"
graph_config = {
    "id": graph_id,
    "name": "Coding Graph",
    "unit": "Minute",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixl_endpoint = f"{graph_endpoint}/{graph_id}"

today = datetime(day=1, month=11,year=2021)

pixl_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "145.50",
}

# response = requests.post(url=pixl_endpoint, json=pixl_config, headers=headers)
# print(response.text)

#-----------------PUT - Update a piece of data-------------------

put_endpoint = f"{pixl_endpoint}/{today.strftime('%Y%m%d')}"

put_config = {
    "quantity": "510.65"
}
# response = requests.put(url=put_endpoint, json=put_config, headers=headers)
# print(response.text)

#-----------------Delete-----DElete a piece of data-------------------

del_endpoint = f"{pixl_endpoint}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=del_endpoint, headers=headers)
# print(response.text)
