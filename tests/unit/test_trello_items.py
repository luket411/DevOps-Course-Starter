from todo_app.data.Item import Item
import todo_app.data.trello_interface
from todo_app.data.trello_interface import parse_trello_response, get_items, add_item, update_from_trello
import pytest
from unittest import mock
from json import loads
from dotenv import load_dotenv, find_dotenv

file_path = find_dotenv('.env.test')
load_dotenv(file_path, override=True)

from tests.conftest import base_json_response


@pytest.mark.parametrize("type, card_details", [
    ("To Do", ["to_do_card_id", "to do card"]),
    ("Doing", ["doing_card_id", "In progress card"]),
    ("Done", ["done_card_id", "Finished card"])
])
def test_parse_trello_response_reads_card_types(type, card_details):

    base_json = loads(base_json_response)

    json_to_parse = [board for board in base_json if board["name"] == type]

    parsed_cards = parse_trello_response(json_to_parse)

    assert len(
        parsed_cards) == 1, f"Incorrect number of cards parsed from base_json"
    assert parsed_cards[0].trello_id == card_details[0]
    assert parsed_cards[0].name == card_details[1]


def test_get_items_updates_from_trello(monkeypatch):
    mock_update_from_trello = mock.MagicMock(
        return_value=loads(base_json_response))
    monkeypatch.setattr(todo_app.data.trello_interface,
                        "update_from_trello", mock_update_from_trello)

    parsed_items = get_items()

    mock_update_from_trello.assert_called()
    assert len(parsed_items) == 3


def test_get_items_parses_trello_items(monkeypatch):
    mock_parse_trello_response = mock.MagicMock()
    monkeypatch.setattr(todo_app.data.trello_interface,
                        "update_from_trello", mock.MagicMock())
    monkeypatch.setattr(todo_app.data.trello_interface,
                        "parse_trello_response", mock_parse_trello_response)

    parsed_items = get_items()

    mock_parse_trello_response.assert_called()
    assert parsed_items == mock_parse_trello_response.return_value, f"parse_items returns"


def test_add_items_makes_correct_request(monkeypatch):
    mock_post_response = mock.MagicMock()
    monkeypatch.setattr(todo_app.data.trello_interface,
                        "post", mock_post_response)
    monkeypatch.setattr(todo_app.data.trello_interface, "update_from_trello",
                        mock.MagicMock(return_value=loads(base_json_response)))

    card_name = "some_new_card"

    response = add_item(card_name)

    mock_post_response.assert_called_once()

    assert "https://api.trello.com/1/cards" in mock_post_response.call_args.args

    given_params = mock_post_response.call_args.kwargs['params']

    assert "some-trello-token" == given_params["token"]
    assert "some-trello-key" == given_params["key"]
    assert "some_new_card" == given_params["name"]
    assert "doing_board_id" == given_params["idList"]


def test_update_from_trello_makes_correct_request(monkeypatch):
    mock_get_response = mock.MagicMock()
    monkeypatch.setattr(todo_app.data.trello_interface,
                        "get", mock_get_response)

    response = update_from_trello()

    mock_get_response.assert_called_once()

    assert f"https://api.trello.com/1/boards/some-trello-board-id/lists" in mock_get_response.call_args.args

    given_params = mock_get_response.call_args.kwargs["params"]

    assert "some-trello-key" == given_params["key"]
    assert "some-trello-token" == given_params["token"]
    assert "open" == given_params["cards"]


def test_update_from_trello_without_cards_makes_correct_response(monkeypatch):
    mock_get_response = mock.MagicMock()
    monkeypatch.setattr(todo_app.data.trello_interface,
                        "get", mock_get_response)

    response = update_from_trello(cards=False)

    mock_get_response.assert_called_once()
    assert "cards" not in mock_get_response.call_args.kwargs["params"]
