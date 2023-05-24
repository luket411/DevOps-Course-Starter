import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
from todo_app.data.ViewModel import ViewModel
from todo_app.data.trello_interface import get_items
from tests.conftest import html_to_ticket_names

from requests import get, post

@pytest.fixture
def client():
    
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    
    test_app = app.create_app()
    
    with test_app.test_client() as client:
        yield client

def test_load_board(client):
    if (status_code := get("https://www.google.com").status_code) != 200:
        pytest.fail(f"No internet connection (status_code = {status_code}). Failing test ...")
    
    pre_html = get("http://localhost:5000").text
    [pre_open_tickets, pre_closed_tickets] = html_to_ticket_names(pre_html)

    items = ViewModel(get_items())
    
    assert len(pre_open_tickets) == len(items.open_items)
    assert len(pre_closed_tickets) == len(items.completed_items)
       
