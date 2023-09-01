def get_todos(filepath='todos.txt'):
    """ Return list of todo items from text file """
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    """ Write to-do items list to text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
