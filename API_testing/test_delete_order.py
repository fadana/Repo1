from requests_folder.delete_order import delete_order
from requests_folder.submit_order import submit_order

class TestDeleteOrder:
		def test_delete_order(self):
				response = delete_order(submit_order(2,"Maria Anton").json()["orderId"])
				assert response.status_code == 204
				assert response.json()==""