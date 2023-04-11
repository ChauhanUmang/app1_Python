import PySimpleGUI as sg
import zip_extrator as ze

sg.theme("Black")

zip_label = sg.Text("Select archive:", key="zip_label")
zip_input_box = sg.Input(key="zip_input_box")
zip_select_button = sg.FileBrowse("Choose", key="zip_choose_btn")

des_label = sg.Txt("Select destination", key="des_label")
des_input_box = sg.Input(key="des_input_box")
des_select_button = sg.FolderBrowse("Choose", key="des_select_btn")

extract_button = sg.Button("Extract", key="extract_btn")
output_label = sg.Text(key="output", text_color="green")

col1 = sg.Column([[zip_label], [des_label]])
col2 = sg.Column([[zip_input_box], [des_input_box]])
col3 = sg.Column([[zip_select_button], [des_select_button]])

window = sg.Window("Archive Extractor",
                   layout=[[col1, col2, col3], [extract_button, output_label]
                           ], font=('Helvetica', 15))

while True:
    event, values = window.read()
    filePath = values["zip_choose_btn"]
    folderPath = values["des_select_btn"]
    ze.zip_extract(filePath, folderPath)
    window["output"].update(value="Extraction completed!")

window.close()
