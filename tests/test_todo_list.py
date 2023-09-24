import pytest
from lib.todo_list import TodoList
from lib.todo import Todo

@pytest.fixture
def todo_list():
    return TodoList()

def test_todo_list_add(todo_list):
    todo1 = Todo("Task 1")
    todo_list.add(todo1)
    assert len(todo_list.incomplete()) == 1

def test_todo_list_incomplete(todo_list):
    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert len(todo_list.incomplete()) == 2

    todo1.mark_complete()
    assert len(todo_list.incomplete()) == 1

def test_todo_list_complete(todo_list):
    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert len(todo_list.complete()) == 0

    todo1.mark_complete()
    assert len(todo_list.complete()) == 1

def test_todo_list_give_up(todo_list):
    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    
    assert len(todo_list.incomplete()) == 0

def test_todo_mark_complete():
    todo = Todo("Task 1")
    assert not todo.complete
    todo.mark_complete()
    assert todo.complete
