class Item():
    def __init__(self, name, trello_id, short_id, trello_list):
        self.name = name
        self.trello_id = trello_id
        self.id = short_id
        self.status = trello_list

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card["name"], card["id"], card["idShort"], list["name"])

    def __repr__(self) -> str:
        return f"Item(name: {self.name}, trello_id: {self.trello_id}, id: {self.id}, status: {self.status})"