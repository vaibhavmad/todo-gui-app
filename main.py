import FreeSimpleGUI as sg
from modules.read_file import read_file
from modules.write_file import write_to_file

label = sg.Text('Enter a ToDo:')
input1 = sg.InputText(tooltip='Enter ToDo', key='todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(values=read_file(), key='todos',
                      enable_events=True, size=[40, 10])
edit_button = sg.Button('Edit')

layout = [[label], [input1, add_button], [list_box, edit_button]]

window = sg.Window('To-Do App', layout, font=('Helvetica', 16))

while True:
    event, values = window.read()
    match event:

        case 'Add':
            todos = read_file()
            new_todo = values['todo']
            todos.append(new_todo)
            write_to_file(todos)
            window['todos'].update(todos)

        case 'Edit':
            todo_to_edit = values['todos'][0]
            todos = read_file()
            todo_index = todos.index(todo_to_edit)
            edited_todo = values['todo'] + '\n'
            todos[todo_index] = edited_todo
            write_to_file(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break
    print(event)
    print(values)
window.close()