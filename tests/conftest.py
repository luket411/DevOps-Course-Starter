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

sample_json_response = """[
  {
    "id": "63ca744738483702fe5d2341",
    "name": "To Do",
    "closed": false,
    "idBoard": "63ca744738483702fe5d233a",
    "pos": 16384,
    "subscribed": false,
    "softLimit": null,
    "status": null,
    "cards": [
      {
        "id": "63ea1a57a262e7d179030fab",
        "badges": {
          "attachmentsByType": {
            "trello": {
              "board": 0,
              "card": 0
            }
          },
          "location": false,
          "votes": 0,
          "viewingMemberVoted": false,
          "subscribed": false,
          "fogbugz": "",
          "checkItems": 0,
          "checkItemsChecked": 0,
          "checkItemsEarliestDue": null,
          "comments": 0,
          "attachments": 0,
          "description": false,
          "due": null,
          "dueComplete": false,
          "start": null
        },
        "checkItemStates": null,
        "closed": false,
        "dueComplete": false,
        "dateLastActivity": "2023-03-01T16:12:39.518Z",
        "desc": "",
        "descData": {
          "emoji": {}
        },
        "due": null,
        "dueReminder": null,
        "email": null,
        "idBoard": "63ca744738483702fe5d233a",
        "idChecklists": [],
        "idList": "63ca744738483702fe5d2341",
        "idMembers": [],
        "idMembersVoted": [],
        "idShort": 4,
        "idAttachmentCover": null,
        "labels": [],
        "idLabels": [],
        "manualCoverAttachment": false,
        "name": "card four",
        "pos": 131071,
        "shortLink": "t67TRrsa",
        "shortUrl": "https://trello.com/c/t67TRrsa",
        "start": null,
        "subscribed": false,
        "url": "https://trello.com/c/t67TRrsa/4-card-four",
        "cover": {
          "idAttachment": null,
          "color": null,
          "idUploadedBackground": null,
          "size": "normal",
          "brightness": "dark",
          "idPlugin": null
        },
        "isTemplate": false,
        "cardRole": null
      },
      {
        "id": "63dced1c03e678b7f9932937",
        "badges": {
          "attachmentsByType": {
            "trello": {
              "board": 0,
              "card": 0
            }
          },
          "location": false,
          "votes": 0,
          "viewingMemberVoted": false,
          "subscribed": false,
          "fogbugz": "",
          "checkItems": 0,
          "checkItemsChecked": 0,
          "checkItemsEarliestDue": null,
          "comments": 0,
          "attachments": 0,
          "description": false,
          "due": null,
          "dueComplete": false,
          "start": null
        },
        "checkItemStates": null,
        "closed": false,
        "dueComplete": false,
        "dateLastActivity": "2023-03-01T16:12:41.319Z",
        "desc": "",
        "descData": {
          "emoji": {}
        },
        "due": null,
        "dueReminder": null,
        "email": null,
        "idBoard": "63ca744738483702fe5d233a",
        "idChecklists": [],
        "idList": "63ca744738483702fe5d2341",
        "idMembers": [],
        "idMembersVoted": [],
        "idShort": 3,
        "idAttachmentCover": null,
        "labels": [],
        "idLabels": [],
        "manualCoverAttachment": false,
        "name": "card three",
        "pos": 196607,
        "shortLink": "mpTLGj8T",
        "shortUrl": "https://trello.com/c/mpTLGj8T",
        "start": null,
        "subscribed": false,
        "url": "https://trello.com/c/mpTLGj8T/3-card-three",
        "cover": {
          "idAttachment": null,
          "color": null,
          "idUploadedBackground": null,
          "size": "normal",
          "brightness": "dark",
          "idPlugin": null
        },
        "isTemplate": false,
        "cardRole": null
      }
    ]
  },
  {
    "id": "63ca744738483702fe5d2342",
    "name": "Doing",
    "closed": false,
    "idBoard": "63ca744738483702fe5d233a",
    "pos": 32768,
    "subscribed": false,
    "softLimit": null,
    "status": null,
    "cards": []
  },
  {
    "id": "63ca744738483702fe5d2343",
    "name": "Done",
    "closed": false,
    "idBoard": "63ca744738483702fe5d233a",
    "pos": 49152,
    "subscribed": false,
    "softLimit": null,
    "status": null,
    "cards": [
      {
        "id": "63dced19969c71c8b90a6267",
        "badges": {
          "attachmentsByType": {
            "trello": {
              "board": 0,
              "card": 0
            }
          },
          "location": false,
          "votes": 0,
          "viewingMemberVoted": false,
          "subscribed": false,
          "fogbugz": "",
          "checkItems": 0,
          "checkItemsChecked": 0,
          "checkItemsEarliestDue": null,
          "comments": 0,
          "attachments": 0,
          "description": false,
          "due": null,
          "dueComplete": false,
          "start": null
        },
        "checkItemStates": null,
        "closed": false,
        "dueComplete": false,
        "dateLastActivity": "2023-03-01T16:24:54.249Z",
        "desc": "",
        "descData": {
          "emoji": {}
        },
        "due": null,
        "dueReminder": null,
        "email": null,
        "idBoard": "63ca744738483702fe5d233a",
        "idChecklists": [],
        "idList": "63ca744738483702fe5d2343",
        "idMembers": [],
        "idMembersVoted": [],
        "idShort": 1,
        "idAttachmentCover": null,
        "labels": [],
        "idLabels": [],
        "manualCoverAttachment": false,
        "name": "card one",
        "pos": 65535,
        "shortLink": "VgP2m54g",
        "shortUrl": "https://trello.com/c/VgP2m54g",
        "start": null,
        "subscribed": false,
        "url": "https://trello.com/c/VgP2m54g/1-card-one",
        "cover": {
          "idAttachment": null,
          "color": null,
          "idUploadedBackground": null,
          "size": "normal",
          "brightness": "dark",
          "idPlugin": null
        },
        "isTemplate": false,
        "cardRole": null
      },
      {
        "id": "63dced1b1b77a62e6b2d4f64",
        "badges": {
          "attachmentsByType": {
            "trello": {
              "board": 0,
              "card": 0
            }
          },
          "location": false,
          "votes": 0,
          "viewingMemberVoted": false,
          "subscribed": false,
          "fogbugz": "",
          "checkItems": 0,
          "checkItemsChecked": 0,
          "checkItemsEarliestDue": null,
          "comments": 0,
          "attachments": 0,
          "description": false,
          "due": null,
          "dueComplete": false,
          "start": null
        },
        "checkItemStates": null,
        "closed": false,
        "dueComplete": false,
        "dateLastActivity": "2023-03-16T11:17:56.545Z",
        "desc": "",
        "descData": {
          "emoji": {}
        },
        "due": null,
        "dueReminder": null,
        "email": null,
        "idBoard": "63ca744738483702fe5d233a",
        "idChecklists": [],
        "idList": "63ca744738483702fe5d2343",
        "idMembers": [],
        "idMembersVoted": [],
        "idShort": 2,
        "idAttachmentCover": null,
        "labels": [],
        "idLabels": [],
        "manualCoverAttachment": false,
        "name": "card two",
        "pos": 131071,
        "shortLink": "QQ3NrUqI",
        "shortUrl": "https://trello.com/c/QQ3NrUqI",
        "start": null,
        "subscribed": false,
        "url": "https://trello.com/c/QQ3NrUqI/2-card-two",
        "cover": {
          "idAttachment": null,
          "color": null,
          "idUploadedBackground": null,
          "size": "normal",
          "brightness": "dark",
          "idPlugin": null
        },
        "isTemplate": false,
        "cardRole": null
      },
      {
        "id": "63ecb236a1e48544ed0d41ad",
        "badges": {
          "attachmentsByType": {
            "trello": {
              "board": 0,
              "card": 0
            }
          },
          "location": false,
          "votes": 0,
          "viewingMemberVoted": false,
          "subscribed": false,
          "fogbugz": "",
          "checkItems": 0,
          "checkItemsChecked": 0,
          "checkItemsEarliestDue": null,
          "comments": 0,
          "attachments": 0,
          "description": false,
          "due": null,
          "dueComplete": false,
          "start": null
        },
        "checkItemStates": null,
        "closed": false,
        "dueComplete": false,
        "dateLastActivity": "2023-03-16T11:18:01.492Z",
        "desc": "",
        "descData": {
          "emoji": {}
        },
        "due": null,
        "dueReminder": null,
        "email": null,
        "idBoard": "63ca744738483702fe5d233a",
        "idChecklists": [],
        "idList": "63ca744738483702fe5d2343",
        "idMembers": [],
        "idMembersVoted": [],
        "idShort": 5,
        "idAttachmentCover": null,
        "labels": [],
        "idLabels": [],
        "manualCoverAttachment": false,
        "name": "card five",
        "pos": 147455,
        "shortLink": "oIyZ9FGl",
        "shortUrl": "https://trello.com/c/oIyZ9FGl",
        "start": null,
        "subscribed": false,
        "url": "https://trello.com/c/oIyZ9FGl/5-card-five",
        "cover": {
          "idAttachment": null,
          "color": null,
          "idUploadedBackground": null,
          "size": "normal",
          "brightness": "dark",
          "idPlugin": null
        },
        "isTemplate": false,
        "cardRole": null
      },
      {
        "id": "63ecbd5026e13108f471ee94",
        "badges": {
          "attachmentsByType": {
            "trello": {
              "board": 0,
              "card": 0
            }
          },
          "location": false,
          "votes": 0,
          "viewingMemberVoted": false,
          "subscribed": false,
          "fogbugz": "",
          "checkItems": 0,
          "checkItemsChecked": 0,
          "checkItemsEarliestDue": null,
          "comments": 0,
          "attachments": 0,
          "description": false,
          "due": null,
          "dueComplete": false,
          "start": null
        },
        "checkItemStates": null,
        "closed": false,
        "dueComplete": false,
        "dateLastActivity": "2023-03-16T11:18:17.569Z",
        "desc": "",
        "descData": {
          "emoji": {}
        },
        "due": null,
        "dueReminder": null,
        "email": null,
        "idBoard": "63ca744738483702fe5d233a",
        "idChecklists": [],
        "idList": "63ca744738483702fe5d2343",
        "idMembers": [],
        "idMembersVoted": [],
        "idShort": 6,
        "idAttachmentCover": null,
        "labels": [],
        "idLabels": [],
        "manualCoverAttachment": false,
        "name": "card six",
        "pos": 163839,
        "shortLink": "8jCih1KD",
        "shortUrl": "https://trello.com/c/8jCih1KD",
        "start": null,
        "subscribed": false,
        "url": "https://trello.com/c/8jCih1KD/6-card-six",
        "cover": {
          "idAttachment": null,
          "color": null,
          "idUploadedBackground": null,
          "size": "normal",
          "brightness": "dark",
          "idPlugin": null
        },
        "isTemplate": false,
        "cardRole": null
      },
      {
        "id": "63f396da92c3f3a099676a28",
        "badges": {
          "attachmentsByType": {
            "trello": {
              "board": 0,
              "card": 0
            }
          },
          "location": false,
          "votes": 0,
          "viewingMemberVoted": false,
          "subscribed": false,
          "fogbugz": "",
          "checkItems": 0,
          "checkItemsChecked": 0,
          "checkItemsEarliestDue": null,
          "comments": 0,
          "attachments": 0,
          "description": false,
          "due": null,
          "dueComplete": false,
          "start": null
        },
        "checkItemStates": null,
        "closed": false,
        "dueComplete": false,
        "dateLastActivity": "2023-03-16T11:18:15.100Z",
        "desc": "",
        "descData": {
          "emoji": {}
        },
        "due": null,
        "dueReminder": null,
        "email": null,
        "idBoard": "63ca744738483702fe5d233a",
        "idChecklists": [],
        "idList": "63ca744738483702fe5d2343",
        "idMembers": [],
        "idMembersVoted": [],
        "idShort": 7,
        "idAttachmentCover": null,
        "labels": [],
        "idLabels": [],
        "manualCoverAttachment": false,
        "name": "card 7",
        "pos": 180223,
        "shortLink": "mIE6aLZC",
        "shortUrl": "https://trello.com/c/mIE6aLZC",
        "start": null,
        "subscribed": false,
        "url": "https://trello.com/c/mIE6aLZC/7-card-7",
        "cover": {
          "idAttachment": null,
          "color": null,
          "idUploadedBackground": null,
          "size": "normal",
          "brightness": "dark",
          "idPlugin": null
        },
        "isTemplate": false,
        "cardRole": null
      }
    ]
  }
]"""