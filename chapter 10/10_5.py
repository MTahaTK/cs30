filename = 'poll.txt'
x = '------------------------------'
while True:
    print(f"{x}\nEnter 'q' or 'quit' at any time to quit.\n{x}")
    reason = input(f"Why do you like programming?\n")
    if reason == 'q' or reason == 'quit':
        print(x)
        break
    else:
        print(x)
        with open(filename, 'a') as file:
            file.write(f"{reason}\n")
        print(x)
        print(f"{reason}")
