import json

# Creates a dictionary from the .json 'pir_eng.json' and stores it in 'lang'
with open('pir_eng.json') as file:
    lang = json.load(file)

x = "----------------------------------------"

# Using the 'lang' dictionary, a title-case dictionary is formed and stored
# in 'caps.'
caps = {}
for k, v in lang.items():
    caps.update({k.title() : v.title()})

# Prompts user to enter a filename for which the program will translate. The
# input is stored in 'file_passage'. The program then tries to read the given
# file, storing it in 'contents.' From here, the passage in the provided file
# is scrubbed through word-by-word and any words that match the keys in the
# original dictionary are replace by their matching translations stored
# individually in 'trans.' This is repeated using the capitalized dictionary.
while True:
    file_passage = input("What file would you like to translate?\n")
    print("Enter 'quit' to end the program.\n")
    print(x)
    if file_passage != 'quit':
        try:
            with open(file_passage, 'r') as file:
                contents = file.read()

            with open(file_passage, 'w') as file:
                    for word in lang:
                        trans = lang[word]
                        contents = contents.replace(word, trans)
                    file.write(contents)

            with open(file_passage, 'w') as file:
                    for word in caps:
                        trans = caps[word]
                        contents = contents.replace(word, trans)
                    file.write(contents)

        # In the event that the provided filename cannot be located, the
        # program informs the user and runs the loop again.
        except FileNotFoundError:
            print("ERROR: File not found. Please enter a valid filename.")
            print(x)
            input("Press 'Enter' to continue.")
            print(x)

        # In the event that the provided file is of an invalid type, the
        # program informs the user and runs the loop again.
        except UnicodeDecodeError:
            print("ERROR: Invalid file type. Please enter a valid filename.")
            print(x)
            input("Press 'Enter' to continue.")
            print(x)

        # If the program encounters no errors, the translation is deemed as
        # successful and the program ends.
        else:
            print("Translation successful.")
            print(x)
            break

    # If the provided input is 'quit,' the program ends.
    else:
        print("Thank you for using this program.")
        print(x)
        break
