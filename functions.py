import os
import json


def load_to_dos(path):
    if os.path.exists(path):
        with open(path, 'r') as todo_load:
            return json.load(todo_load)
    return []

# todosList = load_to_dos()            # Defines

def save_to_dos(todosList, path):
    with open(path, 'w') as todo_save:
        json.dump(todosList, todo_save, indent=4)

def show_to_dos(todosList):
    if not todosList:
        print(f'Your to-do list is empty.')
    else:
        for index, todo in enumerate(todosList, start=1):
            print(f'{index}. {todo.capitalize()}')

def add_to_dos(todo, todosList):
    todosList.append(todo)

def remove_to_dos(todo_index, todosList):
    print('You removed ---', todosList.pop(todo_index - 1), '--- from list.')
