# todos = []
# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f'Today is {now}')
while True:

    user_action: str = input('Type add, edit, show, done or exit: ').strip()  # Remove extra spaces
    if user_action.startswith('add'):
        todo = user_action[4:]
        # todo = input('Enter a todo: ') + "\n"

        todos = functions.get_todos()
        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos()
            num = int(user_action[4:]) - 1
            # num = int(input('Enter todo to edit: '))
            new_todo = input('Enter todo: ') + "\n"
            todos[num] = new_todo

            functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, todo in enumerate(todos):
            print(f'{index + 1}. {todo.strip()}')

    elif user_action.startswith('done'):
        try:
            todos = functions.get_todos()
            index = int(user_action[4:]) - 1
            # index = int(input('Enter completed todo: ')) - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            functions.write_todos(todos)

            print(f'Todo: <{todo_to_remove.strip()}> was removed from the list.')
        except IndexError:
            print('There is no item with that number.')

    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid Command!")
print('Bye! ')

