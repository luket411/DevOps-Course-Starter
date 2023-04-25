from typing import Dict
from sys import path
path.append("/home/tal1yok/repos/devops_training/DevopsCourseRepo")
from todo_app.data.Item import Item

default_item = dict(
    short_id="mock_id",
    name="mock_name",
    trello_list="mock_status",
    trello_id="mock_trello_id"
)

def get_default_item_values(**item):
    new_dict = default_item.copy()
    new_dict.update(item)
    print(new_dict)
    print(default_item)
    return new_dict

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
    return Item(**get_default_item_values(**item))


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

