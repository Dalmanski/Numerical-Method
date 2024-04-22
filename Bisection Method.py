# Example 1: x^3 - 4*x - 9 = 0
# The correct answer is 2.7065, proof? On Yt video: https://www.youtube.com/watch?v=qEecNyRa5o4&t=71s

# Example 2: x^3 + 3*x - 5
# The correct answer is 1.1562, proof? On Yt video: https://www.youtube.com/watch?v=wordn57_Br8

# Example 3: x^3 + 3*x - 2 = 0
# The correct answer is 0.596

import sympy as sp

x = sp.symbols("x")

# Check if it's positive number
def check_pos_num(num): 
    return num >= 0

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

# This is where you input an equation
equation_str = input("Enter your equation: ")
equation_str = equation_str.replace("^", "**")

if "=" in equation_str:
    eqlhs, eqrhs = equation_str.split("=")
    equation_str = eqlhs

equation = sp.sympify(equation_str)

prev_substitute = 0
substitute = 0

# Only next line since print() has automatically \n
print()

""" Repeat until their equally positive and negative number on substitute and prev substitute
    and then it will get the iteration, a = i - 1 and b = i """

i = 0

# Repeat until there's negative and positive result while substitute iteration
while True:

    equation_str = str(equation)
    equation_str = equation_str.replace("x", f"({str(i)})")
    equation_str = equation_str.replace("**", "^")
    
    # Substitute the iteration
    substitute = equation.subs(x, i)

    print(f"f({i}) = {equation_str} = {substitute}")

    # Check if there's positive and negative result
    if (check_pos_num(substitute) != check_pos_num(prev_substitute)) and i != 0:
        break
    
    # Save the current substitute
    prev_substitute = substitute

    i += 1

# 'a' is for iteration - 1
a = i - 1
# While 'b' is for iteration
b = i

print(f"\nSince iteration {a} and {b} have both positive and negative number result, so we use this a = {a} and b = {b}.")

i = 0

""" If substitute is positive, it will replace the b, otherwise it will replace a.
    Repeat until it will approximately equal to the substitute and prev substitute.
    It's also called x_l = a & x_u = b """

print("\nFormula: (a + b) / 2 = x_r")
print("If the answer is negative, put 'a'. While positive, put 'b' \n")

while True:

    i += 1
    print(f"Iteration {i}: \n")

    # This is the formula:
    x_r = (a + b) / 2
    x_r = float(x_r)
    
    # Next, substitute the x of the equation from x_r
    substitute = equation.subs(x, x_r)

    # This is the print-out so it's not important!
    substitute_eq_str = str(equation)
    substitute_eq_str = substitute_eq_str.replace("x", f"({str(x_r)})")
    substitute_eq_str = substitute_eq_str.replace("**", "^")

    print(f"({a} + {b}) / 2 = {shorten_deci(x_r)}")
    print(f"{substitute_eq_str} = {shorten_deci(substitute)} \n")

    # Check if the substitute and preview substitute is equal by rounded up to 3
    if (round(prev_substitute, 3) == round(substitute, 3)):
        break

    # Check if it's positive or negative number
    if (check_pos_num(substitute)):
        b = x_r
        print(f"Since the x_r is positive so b = {x_r}\n")
    else:
        a = x_r
        print(f"Since the x_r is negative so a = {x_r}\n")

    # Save the current substitute
    prev_substitute = substitute

print(f"Final answer: {round(x_r, 3)}\n")

