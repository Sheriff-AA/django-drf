import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": 'Mummy', 'content': 'mom is great'})

print(get_response.json())
