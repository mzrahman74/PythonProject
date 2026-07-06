#print character count with index for input string

text = input("Please enter a number: ")
print("Total Characters: ", len(text))
for index, char in enumerate(text):
    print(f"Index: {index}, Character: {char}")


