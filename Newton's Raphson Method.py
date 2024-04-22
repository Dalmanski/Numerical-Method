# Example 1: x^3 - 4*x^2 + 1 = 0
# The correct answer is 0.5374, proof? On Yt video: https://www.youtube.com/watch?v=-5e2cULI3H8

# Example 2: x^2 - x - 1 = 0
# The correct answer is 1.618, proof? On Yt video: https://www.youtube.com/watch?v=lN1JXolkKCM&t=121s

# Example 3: x^3 - 5
# The correct answer is 1.7099

import sympy as sp

x = sp.symbols("x")

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

equation_str = input("Enter your equation: ")
equation_str = equation_str.replace("^", "**")

if "=" in equation_str:
    eqlhs, eqrhs = equation_str.split("=")
    equation_str = eqlhs

equation = sp.sympify(equation_str)

derivative = sp.diff(equation, x)

print(f"\nDerivative: {derivative} \n")

i = 0
x_i = 1

prev_answer = 0

print(f"Let's say i use x_i = {x_i}\n")

while True:
    
    i += 1
    print(f"Iteration {i}: \n")

    # First, we need to substitute the x_i both your equation and derivative equation
    f = float(equation.subs(x, x_i))
    f_d = float(derivative.subs(x, x_i))

    # Then calculate this using this formula
    answer = float(x_i - (f / f_d))

    print("x_i - (f(x_i) / f'(x_i))")

    # This is the print-out so it's not important!
    print("\nSolving f(x_i)):")
    print(str(equation).replace("**", "^"))
    substitute_eq_str = str(equation)
    substitute_eq_str = substitute_eq_str.replace("x", f"({str(shorten_deci(x_i))})").replace("**", "^")
    print(f"{substitute_eq_str} = {shorten_deci(f)}")

    print("\nSolving f'(x_i):")
    print(str(derivative).replace("**", "^"))
    substitute_eq_str = str(derivative)
    substitute_eq_str = substitute_eq_str.replace("x", f"({str(shorten_deci(x_i))})").replace("**", "^")
    print(f"{substitute_eq_str} = {shorten_deci(f_d)}")

    print(f"\n{shorten_deci(x_i)} - (f({shorten_deci(f)}) / f'({shorten_deci(f_d)}))")
    print(f" = {shorten_deci(answer)}\n")

    # Check if the answer and preview answer is equal by rounded up to 3
    if (round(answer, 3) == round(prev_answer, 3)):
        break

    # Save the current answer
    prev_answer = answer
    # Your answer will transfer to x_i
    x_i = answer

print(f"Final answer: {round(answer, 3)} \n")