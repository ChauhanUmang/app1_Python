from modules import functions as fn
import PySimpleGUI as sgui

label = sgui.Text("Type in a to-do")
input_box = sgui.InputText(tooltip="Enter to-do", key="todo")
add_button = sgui.Button("Add")

window = sgui.Window('My To-Do App',
                     layout=[[label], [input_box, add_button]],
                     font=('Helvetica', 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = fn.get_todos()
            todos.append(values["todo"] + '\n')
            fn.write_todos(todos)
        case sgui.WIN_CLOSED:
            break
window.close()