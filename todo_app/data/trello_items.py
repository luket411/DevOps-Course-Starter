from requests import request
from os import environ
from todo_app.data.Item import Item

list_ids={}

def update_from_trello():
    """
    Fetches all ticket information from Trello
    Returns:
        dict: json response from trello
    """
    url= f"https://api.trello.com/1/boards/{environ['TRELLO_BOARD_ID']}/lists"

    headers = {
        "Accept": "application/json"
    }

    query = {
        "key":environ["TRELLO_KEY"],
        "token":environ["TRELLO_TOKEN"],
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
        "id":<CARD ID_SHORT>
        "status":<TRELLO_LIST THAT CONTAINS CARD>
        "trello_id":<TRELLO_ID>
    }

    Args:
        List: cards on the trello board
    """
    cards = []

    for trello_list in response:
        list_status = trello_list["name"]

        list_ids[list_status] = trello_list["id"]

        for card in trello_list["cards"]:
            cards.append(Item.from_trello_card(card, trello_list))
    
    return cards


def get_items():
    """
    Fetches all saved items from trello.

    Returns:
        list: The list of saved items.
    """
    response = update_from_trello()
    cards = parse_trello_response(response)

    return cards

def add_item(title):
    """
    Adds a new item with the specified title to trello.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    url = "https://api.trello.com/1/cards"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'name': title,
        'idList': list_ids["To Do"],
        'key': environ["TRELLO_KEY"],
        'token': environ["TRELLO_TOKEN"]
    }

    response = request(
        "POST",
        url,
        headers=headers,
        params=query,
        verify=False
    ).json() 

    return response


def change_ticket_list(card_trello_id, target_list):
    """change ticket to new list

    Args:
        card_trello_id: id of ticket to change
        target_list: list to move ticket to

    Returns:
        response
    """
    target_list_id = list_ids[target_list]

    url = f"https://api.trello.com/1/cards/{card_trello_id}"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'idList': target_list_id,
        'key': environ["TRELLO_KEY"],
        'token': environ["TRELLO_TOKEN"]
    }

    response = request(
        "PUT",
        url,
        headers=headers,
        params=query,
        verify=False
    ).json()

    return response
    