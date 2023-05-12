import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import os

import todo_app.data.trello_interface
import requests

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    test_app = app.create_app()
    
    with test_app.test_client() as client:
        yield client

class StubReponse():
    def __init__(self, fake_response_date) -> None:
        self.fake_response_data = fake_response_date

    def json(self):
        return self.fake_response_data


def stub(url, **params):
    
    known_responses = {
        f"https://api.trello.com/1/boards/{os.environ['TRELLO_BOARD_ID']}/lists": [
            {'id': '123abc','name': 'Open','cards': [{'id': '456', 'name': 'Test card', "idShort": 1}]}],
        f"https://api.trello.com/1/cards": []
    }
    
    if url not in known_responses:
        raise Exception(f'Integration test did not expect URL: {url}')
    
    return StubReponse(known_responses[url])


def test_index_page(monkeypatch, client):
    monkeypatch.setattr(todo_app.data.trello_interface, 'get', stub)
    response = client.get('/')
    assert response.status_code == 200
    assert "Test card" in response.data.decode()

def test_create_item_post(monkeypatch, client):
    monkeypatch.setattr(todo_app.app, 'redirect', lambda x: "")
    monkeypatch.setattr(todo_app.data.trello_interface, 'post', stub)
    response = client.post('/')
    assert response.status_code == 200