import os
def test_path_details(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")
test_path_details(r"/Users/olzhikuus/Desktop/MyProject/lab6/dir-and-files/myFile.docx")
# Проверяет, существует ли путь, и выводит директорию и имя файла