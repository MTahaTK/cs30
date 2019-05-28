filenames = ['cats.txt', 'dogs.txt']

for file in filenames:
    try:
        print(f"\nReading {file}...")
        with open(file) as f:
            cont = f.read()
            print(cont)
    except FileNotFoundError:
        print(f"ERROR: FILE '{file}' NOT FOUND")
