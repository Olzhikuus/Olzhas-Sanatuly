import re
need = re.compile('[A-Z][a-z]+')
str = input("Text: ")
check = need.findall(str)
if check:
    print('Found: ', check)
else:
    print('Not found')