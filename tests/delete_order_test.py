import pytest
import requests


def test_order_a_book():
    BASE_URL = 'https://simple-books-api.glitch.me'
    token = 'a4f8ee9ed9d1d1243a6465c90073ae1bf4f4b3112c92044c2162dc1f5076bb40'
    headers = {'Authorization': "Bearer {}".format(token)}
    auth_response = requests.get(BASE_URL, headers=headers)
    print(auth_response.json())
    payload = {'customerName': 'John {{$randomLastName}}'}
    response = requests.delete('https://simple-books-api.glitch.me/orders/:orderId', data=payload)
    books = response.content
    print(books)