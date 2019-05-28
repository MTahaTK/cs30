filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        line = line.replace('Python', 'PHP')
        print(line.rstrip())
