filename = 'guest_book.txt'

while True:
    name = input("Enter 'q' at any time to quit.\nWhat is your name?\n")
    if name == 'q':
        break
    else:
        with open(filename, 'a') as file:
            file.write(f"{name}\n")
        print(f"Hello {name.title()}. You have been added to the guest book.")
