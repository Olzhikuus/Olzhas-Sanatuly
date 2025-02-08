from itertools import permutations

def print_permutations(s):
    perm_list = [''.join(p) for p in permutations(s)]
    for perm in perm_list:
        print(perm)

user_input = input("Enter a string: ")
print("All permutations:")
print_permutations(user_input)