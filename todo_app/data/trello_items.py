from requests import request
from os import environ

TRELLO_KEY = environ["TRELLO_KEY"]
TRELLO_TOKEN = environ["TRELLO_TOKEN"]
TRELLO_BOARD_ID = environ["TRELLO_BOARD_ID"]

def update_from_trello():
    """
    Fetches all ticket information from Trello
    Returns:
        dict: json response from trello
    """
    url= f"https://api.trello.com/1/boards/{TRELLO_BOARD_ID}/lists"

    headers = {
        "Accept": "application/json"
    }

    query = {
        "key":TRELLO_KEY,
        "token":TRELLO_TOKEN,
        "cards":"open"
        }

    response = request(
        "GET",
        url, 
        headers=headers, 
        params=query, 
        verify=False # This is just to get past the corporate proxy I am developing on. I understand not to use this flag if this were production software.
    ).json()
  
    return response


def parse_trello_response(response):
    """ Parses trello response into a list of dictionaries with the form 
    {
        "title":<CARD_NAME>,
        "id":<CARD_ID>,
        "status":<TRELLO_LIST THAT CONTAINS CARD>
    }

    Args:
        List: cards on the trello board
    """

    cards = []

    for trello_list in response:
        list_status = trello_list["name"]
        for card in trello_list["cards"]:
            cards.append({
            "status":list_status,
            "id":card["id"],
            "title":card["name"]
            })
    
    return cards


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    response = update_from_trello()
    cards = parse_trello_response(response)

    return cards


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """

    items = get_items()
    for item in items:
        if item["id"] == id:
            return item
    
    return None


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """


    # Determine the ID for the item based on that of the previously added item
    return


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    return
