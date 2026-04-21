def write_to_file(todo_list, filepath):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_list)
