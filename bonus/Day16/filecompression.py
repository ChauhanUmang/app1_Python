import PySimpleGUI as sg

input_label = sg.Text("Select files to compress:")
input_box = sg.Input()
input_button = sg.FilesBrowse("Choose")

output_label = sg.Text("Select destination folder:")
output_box = sg.Input()
output_button = sg.FolderBrowse()

compress_button  = sg.Button("Compress")

window = sg.Window("File Zipper",
                   layout=[[input_label, input_box, input_button],
                           [output_label, output_box, output_button], [compress_button]])
window.read()
window.close()