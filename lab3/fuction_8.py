def spy_game(numbs):
    s = ''
    for i in numbs:
        s += i
    if '007' in s:
        return True
    return False

numbers = input()
numbs = numbers.split()
print(spy_game(numbs))