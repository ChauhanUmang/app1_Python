import PySimpleGUI as sg
import feettometer as fm

sg.theme("Black")

label_feet = sg.Text("Enter feet")
input_feet = sg.InputText(key="feet")

label_inches = sg.Text("Enter inches")
input_inches = sg.InputText(key="inches")

convert_button = sg.Button("Convert")
output = sg.Text(key="meter")

exit_button = sg.Button("Exit", key="Exit")

window = sg.Window("Convertor", layout=[[label_feet, input_feet],
                                        [label_inches, input_inches],
                                        [convert_button, exit_button, output]])

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

    if values["feet"] == "" or values["inches"] == "":
        sg.popup("Please enter two numbers.", font=('Helvetica', 20))
    else:
        feet = float(values["feet"])
        inches = float(values["inches"])

        result = fm.converttometer(feet, inches)
        window["meter"].update(value=f"{result} m", text_color="green")

window.close()
