import FreeSimpleGUI as sg
from modules.read_file import read_file
from modules.write_file import write_to_file

label = sg.Text('Enter a ToDo:')
input1 = sg.InputText(tooltip='Enter ToDo', key='todo')
add_button = sg.Button("Add")

layout = [[label], [input1, add_button]]

window = sg.Window('To-Do App', layout, font=('Helvetica', 16))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = read_file()
            new_todo = values['todo']
            todos.append(new_todo)
            write_to_file(todos)
        case sg.WIN_CLOSED:
            break
    print(event)
    print(values)
window.close()