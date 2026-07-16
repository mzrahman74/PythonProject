#print character count with index for input string
from z3 import user_prop_eq

text = input("Please enter string: ")
print("Total Characters: ", len(text))
for index, char in enumerate(text):
    print(f"Index: {index}, Character: {char}")


def print_character():
    user_intput = input("Please enter string: ")

    for index1, char1 in enumerate(user_intput):
        print(f"Index: {index1}, Character: {char1}")

print_character()

    

