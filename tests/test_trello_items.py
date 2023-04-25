from todo_app.data.Item import Item
import todo_app.data.trello_items
from todo_app.data.trello_items import parse_trello_response, get_items
import pytest
from unittest import mock
from json import loads


from conftest import base_json_response


@pytest.mark.parametrize("type, card_details", [
    ("To Do", ["to_do_card_id", "to do card"]), 
    ("Doing", ["doing_card_id", "In progress card"]), 
    ("Done", ["done_card_id", "Finished card"])
    ])
def test_parse_trello_response_reads_card_types(type, card_details):

    base_json = loads(base_json_response)

    json_to_parse = [board for board in base_json if board["name"] == type]

    parsed_cards = parse_trello_response(json_to_parse)

    assert len(parsed_cards) == 1, f"Incorrect number of cards parsed from base_json"
    assert parsed_cards[0].trello_id == card_details[0]
    assert parsed_cards[0].name == card_details[1]

def test_get_items_updates_from_trello(monkeypatch):
    mock_update_from_trello = mock.MagicMock(return_value=loads(base_json_response))
    monkeypatch.setattr(todo_app.data.trello_items, "update_from_trello", mock_update_from_trello)

    _ = get_items()

    mock_update_from_trello.assert_called()

def test_get_items_parses_trello_items(monkeypatch):
    mock_parse_trello_response = mock.MagicMock()
    monkeypatch.setattr(todo_app.data.trello_items, "update_from_trello", mock.MagicMock())
    monkeypatch.setattr(todo_app.data.trello_items, "parse_trello_response", mock_parse_trello_response)

    parsed_items = get_items()

    mock_parse_trello_response.assert_called()
    assert parsed_items == mock_parse_trello_response.return_value