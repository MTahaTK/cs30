pizzas = ['cheese', 'margharita', 'vegetable']
friend_pizzas = pizzas[:]
pizzas.append("buffalo debonaire's")
friend_pizzas.append('sumthin')
print(f"My favourite pizzas are: {[x for x in pizzas]}")
print(f"My friend's favourite pizzas are: {[i for i in friend_pizzas]}")
