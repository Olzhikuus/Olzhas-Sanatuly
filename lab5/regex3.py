import re
need = re.compile('[a-z]+_[a-z]+')
str = input("Text: ")
check = need.findall(str)
if check:
    print('Found: ', check)
else:
    print('Not found')