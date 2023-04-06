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

