import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
from tests.conftest import html_to_ticket_names

from requests import get, post

@pytest.fixture
def client():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    
    test_app = app.create_app()
    
    with test_app.test_client() as client:
        yield client

def test_create_ticket(selenium):
    pre_html = get("http://localhost:5000").text
    [pre_open_tickets, pre_closed_tickets] = html_to_ticket_names(pre_html)
    
    
    
    
