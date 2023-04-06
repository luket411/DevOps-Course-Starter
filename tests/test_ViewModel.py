import pytest

from todo_app.data.ViewModel import ViewModel
from todo_app.data.Item import Item

from conftest import get_default_item

def test_empty_ViewModel_can_be_constructed():
    vm = ViewModel([])
    assert vm.items == []

def test_items_returns_all_items():
    open_item = get_default_item(name="some_open_item", trello_list="Open")
    backlog_item = get_default_item(name="some_backlog_item", trello_list="To Do")
    completed_item = get_default_item(name="some_completed_item", trello_list="Done")

    model = ViewModel()
    model._backlog_items = [backlog_item]
    model._open_items = [open_item]
    model._completed_items = [completed_item]

    assert open_item in model.items, "Open items not included in model.items"
    assert backlog_item in model.items, "Backlog items not included in model.items"
    assert completed_item in model.items, "Completed items not included in model.items"

def test_ViewModel_can_be_constructed():
    items = [get_default_item(trello_list=category) for category in ["To Do", "Done", "Doing"]]

    try:
        vm = ViewModel(items)
    except Exception:
        pytest.fail("ViewModel threw error during construction")

    assert len(vm.items) == 3, f"Items missed by ViewModel constructor"


@pytest.mark.parametrize("category", ["backlog", "open", "completed"])
def test_items_getters_return_all_items(category: str):
    # Arrange
    vm = ViewModel([])
    expected_items = ["item1", "item2", "item3"]
    vm.__setattr__(f"_{category}_items", expected_items)

    # Act
    returned_items = vm.__getattribute__(f"{category}_items")

    # Assert
    assert returned_items == expected_items, f"ViewModel.{category}_items doesn't return {category}_items correctly"

@pytest.mark.parametrize("trello_list, category", [("To Do", "backlog"), ("Done", "completed"), ("Doing", "open")])
def test_categories_read(trello_list, category):
    item = Item(name="item1", trello_id="1", short_id="1", trello_list=trello_list)

    vm = ViewModel([item])

    assert vm.__getattribute__(f"_{category}_items") == [item], f"{category}_items not set properly"