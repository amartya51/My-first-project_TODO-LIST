from functions import *

TODO_PATH = r'to_do.json'

def main(path):
    todos = load_to_dos(path)
    while True:

        print('_'*50)
        print('\nWhat do you want to do: ')
        print('1 - Show to do list')
        print('2 - Add new task')
        print('3 - Remove a task')
        print('4 - EXIT')

        choice = input('Please enter command number --->  ')
        # print(choice)        #Experimental feature.
        if choice == '1':
            show_to_dos(todos)
        elif choice == '2':
            task = input('Enter the task you want to add.  ')
            add_to_dos(task, todos)
        elif choice == '3':
            while True:
                wish = input('Do you want to see the list.(y/n)')
                if wish.lower() == 'y':
                    show_to_dos(todos)
                    break
                elif wish.lower() == 'n':
                    break
                else:
                    pass
            choice = input('Enter the task number you want to remove.')
            try:
                remove_to_dos(int(choice), todos)
            except IndexError:
                print('Your to-do list is empty.')
            break
        elif choice == '4':
            break
        else:
            print('Please enter a valid command.')
            continue
    print('_'*50)

if __name__ == '__main__':
    main(TODO_PATH)