import re
need = re.compile('ab*')
str = input("Text: ")
check = need.search(str)
if check:
    print('Found: ', check.group())
else:
    print('Not found')
