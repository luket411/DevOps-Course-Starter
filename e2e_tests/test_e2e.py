import os
import pytest
from time import sleep
from threading import Thread
from todo_app import app
from dotenv import find_dotenv, load_dotenv
from requests import post, delete, get

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_trello_board():
    url = "https://api.trello.com/1/boards/"

    query = {
        'name': 'e2e_test',
        'key': os.environ['TRELLO_KEY'],
        'token': os.environ['TRELLO_TOKEN']
    }

    response = post(
        url,
        params=query,
        verify=False
    ).json()

    return response["id"]


def delete_trello_board(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}"

    query = {
        'key': os.environ['TRELLO_KEY'],
        'token': os.environ['TRELLO_TOKEN']
    }

    response = delete(
        url,
        params=query,
        verify=False
    )

    print(response.text)


@pytest.fixture(scope='module')
def app_with_temp_board():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)

    # Create the new board & update the board id environment variable
    board_id = create_trello_board()
    os.environ['TRELLO_BOARD_ID'] = board_id

    # Construct the new application
    application = app.create_app()

    # Start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    # Give the app a moment to start
    sleep(1)

    yield application

    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)


@pytest.fixture(scope="module")
def driver():

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')

    with webdriver.Chrome(options=chrome_options) as driver:
        yield driver


def test_app_is_running(app_with_temp_board):
    response = get(url="http://localhost:5000")
    assert response.status_code == 200


def test_task_journey(driver, app_with_temp_board):
    driver.get('http://localhost:5000')

    assert driver.title == 'To-Do App'
