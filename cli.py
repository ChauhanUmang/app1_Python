# from functions import get_todos, write_todos
from modules import functions as fn
import time

now = time.strftime("%B %d, %Y %H:%M:%S")
print(f"It is {now}")

while True:
    # Get user input and remove space characters from it.
    user_action = input("Type add, show , edit, complete or exit: ")
    user_action = user_action.strip()

    # if user_action[:3] == 'add' or user_action[:3] == 'new':
    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:] + '\n'

        # we can replace below three line using context-manager
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = fn.get_todos()
        # here we do not have to close the file specifically

        todos.append(todo)

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        fn.write_todos(todos)

    # elif 'show' in user_action[:4]:
    elif user_action.startswith("show"):
        todos = fn.get_todos()

        # new_todos = []

        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # no need to explicitly run a for loop, a single line of list-comprehension is enough
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    # elif 'edit' in user_action[:4]:
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            # get a list of existing todos
            todos = fn.get_todos()

            # Update the existing entry, replaced by new entry
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            # save the file again
            fn.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    # elif 'complete' in user_action[:8]:
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            # fetch a list of existing todos
            todos = fn.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            # save the file
            fn.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    # elif 'exit' in user_action[:4]:
    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print('Bye!')
