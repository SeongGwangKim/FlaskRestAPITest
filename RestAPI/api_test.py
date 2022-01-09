import requests
import json

post_data = [{
                "0" : "temp.jpg",

            }]

#url = 'https://square-flask-api.herokuapp.com/square/'
url = 'http://127.0.0.1:5000/square/'


response = requests.post(url, json=post_data)
print(response)
json_data = json.loads(response.text)
print(response.json())
print(json_data.get("results"))
print(type(json_data))