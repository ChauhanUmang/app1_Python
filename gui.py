from modules import functions as fn
import PySimpleGUI as sgui
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sgui.theme("Black")

clock = sgui.Text("", key="clock")
label = sgui.Text("Type in a to-do")
input_box = sgui.InputText(tooltip="Enter to-do", key="todo")
add_button = sgui.Button("Add")
list_box = sgui.Listbox(values=fn.get_todos(), key="todos", enable_events=True,
                        size=[45, 10])

edit_button = sgui.Button("Edit")
complete_button = sgui.Button("Complete")
exit_button = sgui.Button("Exit")

window = sgui.Window('My To-Do App',
                     layout=[[clock],
                             [label],
                             [input_box, add_button],
                             [list_box, edit_button, complete_button],
                             [exit_button]],
                     font=('Helvetica', 15))
while True:
    event, values = window.read(timeout=2000)
    print(event)
    print(values)
    window["clock"].update(value=time.strftime("%B %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            if values["todo"] != "":
                todos = fn.get_todos()
                todos.append(values["todo"] + '\n')
                fn.write_todos(todos)
                window['todos'].update(values=todos)
            else:
                sgui.popup("Please enter a todo.", font=('Helvetica', 20))
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = fn.get_todos()

                if new_todo != todo_to_edit:
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo + '\n'
                    fn.write_todos(todos)
                    window['todos'].update(values=todos)
                    window['todo'].update(value="")
                else:
                    sgui.popup("You have entered same value.", font=('Helvetica', 20))
            except IndexError:
                sgui.popup("Please select an item first.", font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = fn.get_todos()
                todos.remove(todo_to_complete)
                fn.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sgui.popup("Please select an item first.", font=('Helvetica', 20))
        case "todos":
            window['todo'].update(value=values["todos"][0])
        case "Exit":
            break
        case sgui.WIN_CLOSED:
            break
window.close()