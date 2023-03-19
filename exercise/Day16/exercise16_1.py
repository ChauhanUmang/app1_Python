import PySimpleGUI as sg
import feettometer as fm

label_feet = sg.Text("Enter feet")
input_feet = sg.InputText(key="feet")

label_inches = sg.Text("Enter inches")
input_inches = sg.InputText(key="inches")

convert_button = sg.Button("Convert")
output = sg.Text(key="meter")

window = sg.Window("Convertor", layout=[[label_feet, input_feet],
                                        [label_inches, input_inches],
                                        [convert_button, output]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = fm.converttometer(feet, inches)
    window["meter"].update(value=f"{result} m", text_color="green")

window.close()
