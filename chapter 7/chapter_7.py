# # 7-1
# print("\n7-1")
# user_inp = input("What kind of rental car would you like? ")
# print(f"Let me see if I can find you a {user_inp}.")
#
# # 7-2
# print("\n7-2")
# n = int(input("Welcome. How many people are you dining with? "))
#
# if n > 8:
#     print("I'm sorry, but you will have to wait for a table.")
# else:
#     print("Your table is ready.")
#
# # 7-3
# print("\n7-3")
# num = int(input("Enter a number, and this program will determine" +
#         " whether or not it's a multiple of 10. "))
#
# if num % 10 == 0:
#     print(f"The number {num} is a multiple of 10.")
# else:
#     print(f"The number {num} is not a multiple of 10.")
#
# # 7-4
# print("\n7-4")
#
# prompt = "What toppings do you want on your pizza? "
# prompt += "\nPlease type 'quit' when you are satisfied."
#
# while True:
#     message = input(prompt)
#     if message != "quit":
#         print(f"I will add {message} to your pizza")
#     else:
#         break
# # 7-5
# print("\n7-5")
#
# prompt = "How old are you? "
# prompt += "\nEnter 'quit' when you would like the program to stop. "
#
# while True:
#     inp = input(prompt)
#     if inp != 'quit':
#         if inp < 3:
#             print("Your entry is free of charge.")
#         elif inp >= 3 and inp < 12:
#             print("Your ticket will cost you $10.")
#         elif inp >= 12:
#             print("Your ticket will cost you $15.")
#     else:
#         break
# 7-6
# print("\n7-6")
#
# prompt = "How old are you? "
# prompt += "\nEnter 'quit' when you would like the program to stop. "
#
# active = True
# while active:
#     inp = input(prompt)
#     if inp != 'quit':
#         if inp < 3:
#             print("Your entry is free of charge.")
#         elif inp >= 3 and inp < 12:
#             print("Your ticket will cost you $10.")
#         elif inp >= 12:
#             print("Your ticket will cost you $15.")
#     else:
#         active = False
#
# # 7-7
# print("\n7-7")
#
# while True:
#     resp = input("Type 'yes' for an infinite loop, type 'no' to skip.")
#     if resp != 'no':
#         x = 999
#         while x == x:
#             print("Jebaited")
#     else:
#         break

# 7-8
print("\n7-8")

orders = ['tuna', 'salami', 'chicken', 'turkey', 'beef']
finished_orders = []

while orders:
    finished = orders.pop()
    print(f"I finished your {finished} sandwich.")
    finished_orders.append(finished)
print(finished_orders)

# 7-9
print("\n7-9")

orders = ['tuna', 'pastrami', 'pastrami', 'pastrami', 'salami',
        'chicken', 'turkey', 'pastrami', 'beef' 'pastrami', 'pastrami',]
finished_orders = []

print("The deli has run out of pastrami. We apologize for the" +
    " inconvenience")

while orders:
    while 'pastrami' in orders:
        orders.remove('pastrami')
    finished = orders.pop()
    print(f"I finished your {finished} sandwich.")
    finished_orders.append(finished)
print(finished_orders)

# 7-10
print("\n7-10")

responses = {}
pol_act = True

while pol_act:
    name = input("\nWhat is your name?")
    resp = input("If you could visit one place in the world," +
    " where would you go?")
    responses[name] = resp
    repeat = input("Would you like to let another person respond?" +
    " (yes/no) ")
    if repeat == 'no':
        pol_act = False

print("\n___{|Polling Results|}___ ")
for name, resp in responses.items():
    print(f"{name} would like to go to {resp}.")
