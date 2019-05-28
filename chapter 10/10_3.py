name = input("What is your name?\n")

with open('guest.txt', 'a') as file_object:
    file_object.write(name + '\n')
