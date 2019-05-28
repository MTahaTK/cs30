# 4-1
pizzas = ['cheese', 'margharita', 'vegetable']
for pozzo in pizzas:
    print(f"{pozzo.title()} is pretty neat.")
print("wow")

# 4-2
animals = ['parrot', 'shark', 'rhino', 'monkey']
for animal in animals:
    if animal == 'monkey':
        print(f"Martin is a {animal}")
    else:
        print(f"{animal.title()} is an animal.")
print("All of these animals are endangered aside from Martin, but he'll" +
      " be endangered quite soon.")

# 4-3
[print(x) for x in range(1, 21)]

# 4-4
# million = list(range(1, 1000001))
# [print(x) for x in million]
# 4-5
million = list(range(1, 1000001))

if min(million) == 1 and max(million) == 1000000:
    print(f"{min(million)} \n{max(million)}")
    sum = sum(million)
print(sum)
# 4-6
num = list(range(1, 21, 2))
[print(x) for x in num]
# 4-7
num = list(range(3, 31, 3))
[print(number) for number in num]

# 4-8

# 4-9

# 4-10
million = list(range(1, 1000001))
print(f"The first three items in the list are: {million[0:3]}")
print(f"Three items from the middle of the list are: {million[99:102]}")
print(f"The last three items in the list are: {million[-3:]}")

# 4-11
pizzas = ['cheese', 'margharita', 'vegetable']
friend_pizzas = pizzas[:]
pizzas.append("buffalo debonaire's")
friend_pizzas.append('sumthin')
print(f"My favourite pizzas are: {pizzas}")
print(f"My friend's favourite pizzas are: {friend_pizzas}")

# 4-12
pizzas = ['cheese', 'margharita', 'vegetable']
friend_pizzas = pizzas[:]
pizzas.append("buffalo debonaire's")
friend_pizzas.append('sumthin')
print(f"My favourite pizzas are: {[x for x in pizzas]}")
print(f"My friend's favourite pizzas are: {[i for i in friend_pizzas]}")


dimensions = (200, 50)
[print(dimension) for dimension in dimensions]
