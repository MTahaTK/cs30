import matplotlib.pyplot as plt
from calculator_base import *
from Equation import Expression

# calculator()

msg = "Enter an algebraic expression in mathematical syntax: "
msg += "\nNOTE: MULTIPLICATION MUST USE THE * OPERATOR: "
fn = input(msg)

fn = Expression(fn)
print(fn)
x_values = list(range(1, 1000))
y_values = [fn(x) for x in x_values]
plt.scatter(x_values, y_values, s=40)
plt.axis([0, 10, 0, 500])
plt.show()
