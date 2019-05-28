filename = 'learning_python.txt'

with open(filename) as file_object:
    print(file_object.read().rstrip())

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

contents = ''
for line in lines:
    contents += line

print(contents.strip())
