from todo_app.data.Item import Item
from conftest import get_default_item
import pytest

@pytest.mark.parametrize("param, attribute, value", 
    [
        ("name",        "name",         "some_name"),
        ("trello_id",   "trello_id",    "some_trello_id"),
        ("short_id",    "id",           "some_id"),
        ("trello_list", "status",       "some_status")
    ])
def test_create_item(param, attribute, value):

    item = get_default_item(**{param:value})

    assert item.__getattribute__(attribute) == value, f"Item.{attribute} not set to {value} correctly"


@pytest.mark.parametrize("attribute, expected_value, card_changes, list_changes",
    [
        ("name", "some_test_card_name", dict(name="some_test_card_name"), dict()),
        ("trello_id", "some_test_id", dict(id="some_test_id"), dict()),
        ("id", "some_test_short_id", dict(idShort="some_test_short_id"), dict()),
        ("status", "some_test_list_name", dict(), dict(name="some_test_list_name"))
    ])
def test_from_trello_card(attribute, expected_value, card_changes, list_changes):
    mock_card = dict(name="mock_card_name", id="mock_id", idShort="mock_id_short")
    mock_list = dict(name="mock_list_name")

    mock_card.update(card_changes)
    mock_list.update(list_changes)

    item = Item.from_trello_card(mock_card, mock_list)

    assert item.__getattribute__(attribute) == expected_value, f"Item.{attribute} not set to {expected_value}"