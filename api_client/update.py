import requests

endpoint = "http://localhost:8000/api/products/6/update/"

data = {
    "title": "Twin 4",
    "price": 5.99,
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
