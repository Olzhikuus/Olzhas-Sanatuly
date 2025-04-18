from docx import Document

def count_docx_lines(file_path):
    doc = Document(file_path)
    return len(doc.paragraphs)

print("Number of lines:", count_docx_lines("/Users/olzhikuus/Desktop/MyProject/lab6/dir-and-files/myFile.docx"))
# Считает количество параграфов (строк) в .docx-файле