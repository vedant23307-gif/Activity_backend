import requests
import pandas as pd
import json

# Your API endpoint
url = "http://localhost:8000/excel/create"

# Your data to send
frame=({
    'name':['om'],
    'roll':[54],
    'mark':[34]
})
df=pd.DataFrame(frame)
data = df.to_dict(orient='records')
# Send POST request
response = requests.post(url, json=data)

# Print the response
print("Status code:", response.status_code)
print("Response JSON:", response.json())
