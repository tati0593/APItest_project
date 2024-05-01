import pytest
import requests


def test_books_list():
    response = requests.get("https://simple-books-api.glitch.me/books")
    books = response.content
    print(books)

