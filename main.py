import FreeSimpleGUI as sg
from modules.read_file import read_file
from modules.write_file import write_to_file

label = sg.Text('Enter a ToDo:')
input1 = sg.InputText(tooltip='Enter ToDo', key='todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(values=read_file(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')

layout = [[label], [input1, add_button], [list_box, edit_button]]

window = sg.Window('To-Do App', layout, font=('Helvetica', 16))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = read_file()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            write_to_file(todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = read_file()
            index_of_todo_to_edit = todos.index(todo_to_edit)
            todos[index_of_todo_to_edit] = new_todo + '\n'
            write_to_file(todos)
            window['todos'].update(values=todos)
        case sg.WIN_CLOSED:
            break

window.close()