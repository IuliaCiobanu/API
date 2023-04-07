import requests
from requests_folder.get_token import generate_token

def submit_order(book_id, customer_name):
    request_body = {
            "bookId": book_id,
            "customerName": customer_name
        }
    token = generate_token()
    header_params = {'Authorization': token}
    r = request.post( 'https://simple-books-api.glitch.me/orders', json=request_body, headers=header_params )
    return r
