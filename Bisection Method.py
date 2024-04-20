import sympy as sp

x = sp.symbols("x")

equation_str = input("Enter your equation: ")
equation_str = equation_str.replace("^", "**")

if "=" in equation_str:
    eqlhs, eqrhs = equation_str.split("=")
    equation_str = eqlhs

equation = sp.sympify(equation_str)

prev_substitute = 0
substitute = 0

print()

# Check if it's positive number
def check_pos_num(num): 
    return num >= 0

i = 0

""" Repeat until their equally positive and negative number on substitute and prev substitute
    and then it will get the iteration, a = i - 1 and b = i """

while True:

    equation_str = str(equation)
    equation_str = equation_str.replace("x", str(i))
    
    # Substitute the iteration
    substitute = equation.subs(x, i)

    print(f"f({i}) = {equation_str} = {substitute}")

    if (check_pos_num(substitute) != check_pos_num(prev_substitute)) and i != 0:
        break
    prev_substitute = substitute
    i += 1

a = i - 1
b = i

print(f"\nSince iteration {a} and {b} have both positive and negative number so we use this a = {a} and b = {b}.")

i = 0

print()

""" If substitute is positive, it will replace the b, otherwise it will replace a.
    Repeat until it will approximately equal to the substitute and prev substitute """

print("Formula: (a + b) / 2 = x_1 \n")

while True:

    i += 1
    print(f"Iteration {i}: \n")

    x_1 = float((a + b) / 2)
    
    print(f"({a} + {b}) / 2 = {x_1}")

    substitute = equation.subs(x, x_1)

    substitute_str = str(equation)
    substitute_str = substitute_str.replace("x", f"({str(x_1)})")

    print(f"{substitute_str} = {substitute} \n")

    if (round(prev_substitute, 3) == round(substitute, 3)):
        break

    if (check_pos_num(substitute)):
        b = x_1
    else:
        a = x_1

    prev_substitute = substitute

print(f"Final answer: {round(x_1, 3)}")

