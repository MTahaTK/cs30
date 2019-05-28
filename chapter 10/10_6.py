num = []
try:
    first = input("Pick any number: ")
    second = input("Pick another number: ")
    sum = int(first) + int(second)
    print(f"{first} + {second} = {sum}")
except ValueError:
    print("Please provide number inputs only.")
