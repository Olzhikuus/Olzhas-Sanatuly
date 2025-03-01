import re
need = re.compile('ab{2,3}')
str = input("Text: ")
check = need.search(str)
if check:
    print('Found: ',check.group())
else:
    print('Not found')