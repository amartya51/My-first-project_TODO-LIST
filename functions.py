import os
import json


def load_to_dos(path):
    if os.path.exists(path):
        with open(path, 'r') as todo_load:
            return json.load(todo_load)
    return []

todos = load_to_dos()            # Defines

def save_to_dos(todos, path):
    with open(path, 'w') as todo_save:
        json.dump(todos, todo_save, indent=4)

def show_to_dos(todos):
    if not todos:
        print(f'Your to-do list is empty.')
    else:
        for index, todo in enumerate(todos, start=1):
            print(f'{index}. {todo.capitalise()}')

def add_to_dos(todo):
    todos.append(todo)

def remove_to_dos(todo_index):
    print('You removed ---', todos.pop(todo_index - 1), '--- from list.')
