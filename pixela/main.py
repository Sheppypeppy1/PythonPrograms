import requests

USERNAME = "sheppypeppy"
TOKEN = "98345o34o3jo34i5jo"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : "graph1",
    "name" : "Workout Graph",
    "unit" : "commit",
    "type" : "int",
    "color" : "sora"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)