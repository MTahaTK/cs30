# Course: CS 30
# Period: 2
# Date created: 19/03/05
# Date last modified: 19/03/06
# Name: Taha Khokhar
# Description: A token generator that makes use of user input to both
# determine how long the token should be in bytes and what kind of token
# should be generated.

# Imports the 'secrets' module from the Python Standard Library
import secrets

# Stores integer user input in the variable "numbytes" as the number of bytes
# that should make up the token.
numbytes = int(input("How many bytes would you like to make up your tokens? "))

# Storing three types of tokens available in 'secrets' - random byte strings,
# hexadecimals, and url-safe text strings - in a tuple for use later in the
# program.
types = ('random byte string', 'hexadecimal', 'url-safe text string')

# This essentially functions to continuously prompt the user to input a valid
# token type in the following user input line until a valid token type is
# provided. Once this condition is true, an if-elif-else block is evaluated.
# When any of these evaluate to true, the token is printed and the program
# breaks. Otherwise, the loop repeats again, alongside a printed message.
while True:
    token_inp = str(input("What type of token would you like to generate? " +
                    f"\nYou can choose from the following types: {types}: "))
    if token_inp == 'random byte string':
        print(secrets.token_bytes(numbytes))
        break
    elif token_inp == 'hexadecimal':
        print(secrets.token_hex(numbytes))
        break
    elif token_inp == 'url-safe text string':
        print(secrets.token_urlsafe(numbytes))
        break
    else:
        print("Please select a valid token type")
