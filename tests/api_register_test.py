import pytest
import requests


def test_register_client():
    payload = {'clientName': 'Tatiana', 'clientEmail': 'tatiana_torres05@hotmail.com'}
    r = requests.post('https://simple-books-api.glitch.me/api-clients', data=payload)
    print(r.text)
