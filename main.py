import FreeSimpleGUI as sg
from modules.read_file import read_file
from modules.write_file import write_to_file

try:
    to_do_file = read_file('files/todos.txt')
except FileNotFoundError:
    with open('files/todos.txt', 'w') as file:
        pass

try:
    complete_todo_file = read_file('files/complete_todo.txt')
except FileNotFoundError:
    with open('files/complete_todo.txt', 'w') as file:
        pass

add_todo_label = sg.Text('Add ToDo:')
add_todo_input = sg.InputText(key='add_todo')
add_todo_button = sg.Button('Add')

display_todo = sg.Listbox(values=[], key='todos_box', enable_events=True, size=[30, 10])
display_completed_todo = sg.Listbox(values=[], key='completed', size=[30, 10])

edit_todo_button = sg.Button('Edit')
complete_todo_button = sg.Button('Complete')
delete_todo_button = sg.Button('Delete')
refresh_all_button = sg.Button('Refresh')
exit_app_button = sg.Button('Exit')

layout = [[add_todo_label, add_todo_input, add_todo_button],
          [display_todo, display_completed_todo],
          [edit_todo_button, complete_todo_button, delete_todo_button, refresh_all_button, exit_app_button]]

window = sg.Window(title='ToDo App',layout=layout,finalize=True)

window['add_todo'].bind('<Return>', 'ENTER')

todos = read_file('files/todos.txt')
window['todos_box'].update(values=todos)

completed_list = read_file('files/complete_todo.txt')
window['completed'].update(values=completed_list)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'add_todoENTER' | 'Add':
            todo = values['add_todo']  + '\n'
            todos = read_file('files/todos.txt')
            todos.append(todo)
            write_to_file(todos, 'files/todos.txt')
            window['todos_box'].update(values=todos)

        case 'Complete':
            todo_to_complete = values['todos_box'][0]
            todos = read_file('files/todos.txt')
            todo_complete_index = todos.index(todo_to_complete)
            completed_todo = todos.pop(todo_complete_index)
            write_to_file(todos, 'files/todos.txt')
            window['todos_box'].update(values=todos)
            completed_list = read_file('files/complete_todo.txt')
            completed_list.append(completed_todo)
            write_to_file(completed_list, 'files/complete_todo.txt')
            window['completed'].update(values=completed_list)

        case sg.WIN_CLOSED | 'Exit':
            break

window.close()
