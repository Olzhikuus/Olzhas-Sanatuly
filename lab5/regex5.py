import re
need = re.compile('^a.*b$')
str = input("Text: ")
check = need.match(str)
if check:
    print('Found: ', check.group())
else:
    print('Not found')