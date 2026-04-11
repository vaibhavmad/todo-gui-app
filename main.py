import FreeSimpleGUI as sg

label = sg.Text('Enter a ToDo:')
input1 = sg.InputText(tooltip='Enter ToDo')
add_button = sg.Button("Add")

window = sg.Window('To-Do App', layout=[[label], [input1, add_button]])
window.read()
window.close()