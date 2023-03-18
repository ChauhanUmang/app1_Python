import glob

myfiles = glob.glob("files/**/*.txt")
files_list = []

for file_content in myfiles:
    with open(file_content, 'r') as file:
        print(file.read().upper())

for filePath in myfiles:
    parts = filePath.split("\\")
    files_list.append(parts[2])

print(files_list)

