num = []
while True:
    try:
        first = input("Pick any number: ")
        second = input("Pick another number: ")
        sum = int(first) + int(second)
        print(f"{first} + {second} = {sum}")
        break
    except ValueError:
        print("Please provide number inputs only.")
