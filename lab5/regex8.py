import re
def split(str):
    word = re.findall('[A-Z][a-z]*',str)
    return word
str = input("Text:")
result = split(str)
print(result)