import requests
import random

def generate_token():
    nr = random.randint(1,99999999999)
    request_body = {
        "clientName": "Postman",
        "clientEmail": f"ZAZ{nr}@example.com"
    }
    r = requests.post('https://simple-books-api.glitch.me/api-clients/', json=request_body)
    token = r.json()['accessToken']
    return token