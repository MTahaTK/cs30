import matplotlib
from calculator_base import *
from Equation import Expression

# calculator()

msg = "Enter an algebraic expression in mathematical syntax: "
msg += "\nNOTE: MULTIPLICATION MUST USE THE * OPERATOR: "
fn = input(msg)

fn = Expression(fn)
print(fn)
print(fn(3))
