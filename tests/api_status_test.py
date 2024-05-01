import pytest
import requests


def test_api_status():
    response = requests.get("https://simple-books-api.glitch.me")
    status = response.status_code
    assert status == 200
    print(status)



