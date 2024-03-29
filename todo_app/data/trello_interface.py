from requests import get, post, put
from os import environ
from todo_app.data.Item import Item


def update_from_trello(cards=True):
    """
    Fetches all ticket information from Trello
    Returns:
        dict: json response from trello
    """
    url = f"https://api.trello.com/1/boards/{environ['TRELLO_BOARD_ID']}/lists"

    headers = {
        "Accept": "application/json"
    }

    query = {
        "key": environ["TRELLO_KEY"],
        "token": environ["TRELLO_TOKEN"],
    }

    if cards:
        query["cards"] = "open"

    response = get(
        url,
        headers=headers,
        params=query,
        # If the USE_SSL environment variable is set then SSL is used. By default it is not in order to work around a proxy server
        verify="USE_SSL" in environ
    ).json()

    return response


def parse_trello_response(response):
    """ Parses trello response into a list of Item objects

    Args:
        List: cards on the trello board
    """
    cards = []

    for trello_list in response:

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


def get_list_ids():
    """Gets list ids from trello

    Returns:
        list_ids: dict that maps name of lists to trello list ids

    """

    trello_response = update_from_trello(cards=False)

    lists = {list["name"]: list["id"] for list in trello_response}

    return lists


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

    list_ids = get_list_ids()

    query = {
        'name': title,
        'idList': list_ids["Doing"],
        'key': environ["TRELLO_KEY"],
        'token': environ["TRELLO_TOKEN"]
    }

    response = post(
        url,
        headers=headers,
        params=query,
        # If the USE_SSL environment variable is set then SSL is used. By default it is not in order to work around a proxy server
        verify="USE_SSL" in environ
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
    list_ids = get_list_ids()

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

    response = put(
        url,
        headers=headers,
        params=query,
        # If the USE_SSL environment variable is set then SSL is used. By default it is not in order to work around a proxy server
        verify="USE_SSL" in environ
    ).json()

    return response
