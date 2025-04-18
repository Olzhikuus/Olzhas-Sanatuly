import re
need = re.compile('[ ,.]')
str = input("Text: ")
result = re.sub(need, ":" , str)
print(result)

# Замена пробелов, запятых и точек на ":"