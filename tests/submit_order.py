from requests_folder.get_token import *
from requests_folder.submit_order import submit_order

class TestSubmitOrder:
    def test_submit_order(self):
        r.submit_order(1,"John")
        assert r.status_code==201, f"Error: Status code error Expected:201, Actual:{r.status_code}"
        assert r.json()["created"]=="true", f"Error: The order was not created. Created: {r.json()['created']}"
        assert len(r.json()["orderId"])>0, f"Error: Order ID is invalid. Actual orderId: {r.json()['orderId']}"

    def test_submit_order1(self):
        r.submit_order(9,"John")
        assert r.status_code==400, f"Error: Status code error Expected:400, Actual:{r.status_code}"
        assert r.json()["error"]=="Invalid or missing bookId."
        assert len(r.json()["orderId"])>0, f"Error: Order ID is invalid. Actual orderId: {r.json()['orderId']}"
