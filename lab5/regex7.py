import re

def upper(match):
    return match.group(1).upper()

def convert_snake_to_camel(snake1):
    camel1 = re.sub(r'_([a-zA-Z])', upper, snake1)
    return camel1


snake = input("Text: ")
camel = convert_snake_to_camel(snake)
print(camel)