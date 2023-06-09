class ViewModel():
    def __init__(self, all_items=[]) -> None:
        self._backlog_items = [item for item in all_items if item.status == "To Do"]
        self._completed_items = [item for item in all_items if item.status == "Done"]
        self._open_items = [item for item in all_items if item.status == "Doing"]

    @property
    def open_items(self):
        return self._open_items

    @property
    def completed_items(self):
        return self._completed_items
    
    @property
    def backlog_items(self):
        return self._backlog_items

    @property
    def items(self):
        return self._backlog_items + self._completed_items + self._open_items