import requests
import random

def generate_token():
		nr = random.randint(1,99999999999999999999)
		request_body = {
						"clientName": "Razvan Maxim",
						"clientEmail": f"razvan.maxim{nr}@gmail.com"
		}
		response = requests.post("https://simple-books-api.glitch.me/api-clients/",json=request_body)
		token = response.json()["accessToken"]
		return token