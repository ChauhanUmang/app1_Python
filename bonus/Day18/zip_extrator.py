import zipfile


def zip_extract(zippath, folder):
    with zipfile.ZipFile(zippath, 'r') as file:
        file.extractall(folder)


if __name__ == "__main__":
    zip_extract("E:/Coding/python_py_charm/app1/bonus/Day16/compressed.zip",
                "E:/Coding/python_py_charm/app1/bonus/Day18")
