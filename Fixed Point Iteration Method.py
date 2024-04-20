import sympy as sp
from sympy import *

x = sp.symbols("x")

equation_str = input("Enter your equation: ")
equation_str = equation_str.replace("^", "**")

eqlhs, eqrhs = equation_str.split('=')
equation = sp.Eq(sympify(eqlhs), sympify(eqrhs))

""" There are 2 methods to simplify but I'll go with this one... """

# Simplify the equation, then factor out
equation = sp.simplify(equation)
print(sp.pretty(equation))
equation = sp.factor(equation)
print(sp.pretty(equation))

# Lastly divided it to make x variable left in left-side and divided on the right-side
divided_by = sp.sympify('(' + str(equation.lhs / x) + ')')
eqlhs = equation.lhs / divided_by
eqrhs = equation.rhs / divided_by
equation = sp.Eq(eqlhs, eqrhs)

print("Simplify equation: \n", sp.pretty(equation), "\n")

i = 0
x_new = 0
gx = 0
prev_gx = 0

while True:

    i += 1
    print(f"Iteration {i}:")

    print(str(equation.rhs).replace("x", str(x_new)))

    gx = float(equation.rhs.subs(x, x_new))
    print(gx, "\n")
    
    if (round(gx, 3) == round(prev_gx, 3)):
        break

    prev_gx = gx
    x_new = gx

print(f"Final answer: {round(gx, 3)}")