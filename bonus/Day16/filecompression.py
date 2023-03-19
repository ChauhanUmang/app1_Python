import PySimpleGUI as sg
import zip_creator as zc

input_label = sg.Text("Select files to compress:")
input_box = sg.Input()
input_button = sg.FilesBrowse("Choose", key="files")

output_label = sg.Text("Select destination folder:")
output_box = sg.Input()
output_button = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
compress_label = sg.Text(key="compress_label", text_color="green")

window = sg.Window("File Zipper",
                   layout=[[input_label, input_box, input_button],
                           [output_label, output_box, output_button], [compress_button, compress_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder_path = values["folder"]
    zc.make_archive(filepaths, folder_path)
    window["compress_label"].update(value="Compression completed")


window.close()
