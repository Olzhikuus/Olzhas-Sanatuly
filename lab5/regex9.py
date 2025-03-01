import re
def insert(str):
    ins = re.sub('(?=[A-Z])', ' ', str)
    return ins
str = input("Text: ")
result = insert(str)
print(result)