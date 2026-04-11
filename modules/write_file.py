FILEPATH = '../todos.txt'


def write_to_file(todo_list, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_list)
