import sympy as sp
from sympy import *

x = sp.symbols("x")

# Example 1: x^2 - x - 1 = 0
# The correct answer is -0.618 and 1.618, proof? On Yt video: https://www.youtube.com/watch?v=L321onHPn4U&t=954s

""" !!! There's an error on some equations due to inaccuracy of simplifying lol !!! """

equation_str = input("Enter your equation: ")
equation_str = equation_str.replace("^", "**")

def shorten_deci(num, precision=3):
    num = float(num)
    num_str = str(num)
    decimal_part = num_str.split('.')[1]
    if len(set(decimal_part)) == 1:
        num_str = num_str.rstrip('0').rstrip('.')  # Remove zeros after decimal
        if decimal_part == '0':  # Check if the decimal part is zero
            return str(int(num))  # Return the integer part if the decimal part is zero
        else:
            return str("{:.{}f}".format(float(num_str), precision))
    else:
        return str(num)

""" There are 2 methods to simplify but I'll go with this one... """

for m in range(1, 3):
    
    if "=" in equation_str:
        eqlhs, eqrhs = equation_str.split('=')
    else:
        eqlhs = equation_str
        eqrhs = 0
    
    equation = sp.Eq(sympify(eqlhs), sympify(eqrhs))

    print(f"\n================ Method {m} ================\n")

    # Method 1 (mostly this is success)
    if m == 1:
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

    # Method 2 (Most of equation will broken probably...)
    elif m == 2:
        # Move x^2 to left-side and remove x^2 on right-side
        divided_by = sp.sympify('(' + str(equation.lhs).replace("x**2", "") + ')')
        eqlhs = equation.lhs - divided_by
        eqrhs = equation.rhs - divided_by
        equation = sp.Eq(eqlhs, eqrhs)
        print(sp.pretty(equation))

        # Divided by x on both side from x^2 to x
        eqlhs = equation.lhs / x
        eqrhs = equation.rhs / x
        equation = sp.Eq(eqlhs, eqrhs)

    print("Simplify equation: \n", sp.pretty(equation), "\n")

    i = 0
    x_new = 0.5
    gx = 0
    prev_gx = 0
    
    print(f"Let's say i use x_new = {x_new}\n")

    while True:

        more_than_20 = False

        i += 1
        print(f"Iteration {i}:")

        print(f"{equation.lhs} = {equation.rhs}")
        print(f"x = {str(equation.rhs).replace("x", str(shorten_deci(x_new)))}")

        # First, substitute the x_new on equation
        gx = float(equation.rhs.subs(x, x_new))

        print(f"x = {shorten_deci(gx)}", "\n")
        
        if (round(gx, 3) == round(prev_gx, 3)):
            break
        elif i > 19:
            more_than_20 = True
            break

        # Save the current gx
        prev_gx = gx
        # Your gx will transfer to x_new
        x_new = gx

    if not more_than_20:
        print(f"Final answer: {round(gx, 3)}\n")
    else:
        print(f"Cannot find accurate answer but here ya go: {round(gx, 3)}\n")