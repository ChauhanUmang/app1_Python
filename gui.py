from modules import functions as fn
import PySimpleGUI as sgui

label = sgui.Text("Type in a to-do")
input_box = sgui.InputText(tooltip="Enter to-do", key="todo")
add_button = sgui.Button("Add")
list_box = sgui.Listbox(values=fn.get_todos(), key="todos", enable_events=True,
                        size=[45, 10])

edit_button = sgui.Button("Edit")
complete_button = sgui.Button("Complete")
exit_button = sgui.Button("Exit")

window = sgui.Window('My To-Do App',
                     layout=[[label],
                             [input_box, add_button],
                             [list_box, edit_button, complete_button],
                             [exit_button]],
                     font=('Helvetica', 15))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = fn.get_todos()
            todos.append(values["todo"] + '\n')
            fn.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = fn.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            fn.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = fn.get_todos()
            todos.remove(todo_to_complete)
            fn.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "todos":
            window['todo'].update(value=values["todos"][0])
        case "Exit":
            break
        case sgui.WIN_CLOSED:
            break
window.close()