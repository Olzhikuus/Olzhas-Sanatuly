import re

def ctos(text): 
    tosanke = re.sub(r'([a-z])([A-Z])', r'\1_\2', text)  
    return tosanke.lower() 

text = input("Text: ")
result = ctos(text)
print(result)