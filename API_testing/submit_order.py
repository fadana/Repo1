import requests

from requests_folder.get_token import generate_token

def submit_order(bookid, customer_name):
		request_body = {
				"bookId":bookid,
				"customerName":customer_name
		}
		token = generate_token()
		header_params = {'Authorization':token}
		response = requests.post("https://simple-books-api.glitch.me/orders",json = request_body, headers= header_params)
		return 