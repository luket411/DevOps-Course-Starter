from re import findall
from sys import path

from todo_app.data.Item import Item


def get_default_item(**item):
    """Returns mock item to use for testing. Provide parameters to specify values and it will mock the rest

    Args:
        short_id (str): Item.id
        name (str): Item.name
        trello_id (str): Item.trello_id
        trello_list (str): Item.status

    Returns:
        _type_: _description_
    """
    return Item(
        item.get("name", "mock_name"),
        item.get("trello_id", "mock_id"),
        item.get("short_id", "mock_short_id"),
        item.get("trello_list", "mock_trello_list"),
    )


base_json_response = """[
    {
        "id": "to_do_board_id",
        "name": "To Do",
        "cards":[
            {
                "id": "to_do_card_id",
                "name": "to do card",
                "idShort": 1
            }
        ]
    },
    {
        "id": "doing_board_id",
        "name": "Doing",
        "cards":[
            {
                "id": "doing_card_id",
                "name": "In progress card",
                "idShort": 2
            }
        ]
    },
    {
        "id": "done_board_id",
        "name": "Done",
        "cards":[
            {
                "id": "done_card_id",
                "name": "Finished card",
                "idShort": 3
            }
        ]
    }
]"""


def html_to_ticket_names(html_in):
    """Takes a html page of the todo app and returns an array of open items and an array of closed items

    Args:
        html_in (str): html in

    Returns:
        tickets ([[open_items],[closed_items]])
    """
    def find_ticket_name(tag):
        return tag.split(">")[1].split("<")[0].strip()

    open_tickets_raw = findall(
        "<a href=\"/complete-item/[\w]*\">\s[^<]*</a>", html_in)
    closed_tickets_raw = findall(
        "<a href=\"/reopen-item/[\w]*\">\s[^<]*</a>", html_in)

    open_tickets = [find_ticket_name(tag) for tag in open_tickets_raw]
    closed_tickets = [find_ticket_name(tag) for tag in closed_tickets_raw]

    return [open_tickets, closed_tickets]
