# Course: CS 30
# Period: 2
# Date created: 19/03/05
# Date last modified: 19/03/06
# Name: Taha Khokhar
# Description:

import secrets

bytes = int(input("How many bytes would you like to make up your tokens? "))

token_types = ['random byte string', 'hexadecimal', 'url-safe text string']

# for type in token_types:
while True:
    token_inp = str(input("What type of token would you like to generate? " +
    f"\nYou can choose from the following types: {token_types}:"))
    if token_inp == type:
        if token_inp == 'random byte string':
            print(secrets.token_bytes(bytes))
            break
        elif token_inp == 'hexadecimal':
            print(secrets.token_hex(bytes))
            break
        elif token_inp == 'url-safe text string':
            print(secrets.token_urlsafe(bytes))
            break
    else:
        print("Please select a valid token type")
