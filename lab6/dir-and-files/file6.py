import string
def generate_26_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            pass
generate_26_files()
# Создаёт 26 пустых текстовых файлов по алфавиту (A.txt до Z.txt)