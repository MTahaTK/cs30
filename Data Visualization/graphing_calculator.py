import matplotlib.pyplot as plt
from calculator_base import *
from Equation import Expression

# calculator()

# msg = "Enter an algebraic expression in mathematical syntax: "
# msg += "\nNOTE: MULTIPLICATION MUST USE THE * OPERATOR: "
# fn = input(msg)

# fn = Expression(fn)
# print(fn)
# x_values = list(range(1, 100))
# y_values = [fn(x) for x in x_values]
# plt.plot(x_values, y_values)
# plt.show()

expression, x='' = input().split(", ")
print(expression)
expression = str(expression)
if x != '':
    x = float(x)
else:
    x = ''
eval_expression(expression, x)
