filenames = ['cats.txt', 'dogs.txt']

for file in filenames:
    try:
        with open(file) as f:
            cont = f.read()

    except FileNotFoundError:
        pass
    else:
        print(f"\nReading {file}...")
        print(cont)
