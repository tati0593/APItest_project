import pytest
import requests


def test_single_book():
    response = requests.get("https://simple-books-api.glitch.me/books/:bookId?bookId=1")
    books = response.content
    print(books)
