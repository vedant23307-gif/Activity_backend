import requests
import json

# Your API endpoint
url = "http://localhost:8000/json/create"

# Your data to send
data = {
    "name": "Vedant",
    "age": 21
}

# Send POST request
response = requests.post(url, json=data)

# Print the response
print("Status code:", response.status_code)
print("Response JSON:", response.json())
