# Example 1: x^2 - x - 1 = 0, x_a = 3, x_b = 2
# The correct answer is 1.618, proof? On Yt video: https://www.youtube.com/watch?v=AN6YxAoUqLM&t=435s
# Example 2: x^4 - x - 10, x_a = 1, x_b = 2
# The correct answer is 1.856, proof? On Yt video: https://www.youtube.com/watch?v=3g19OMfCpCA
# Example 3: x^2 - 2, x_a = 1, x_b= 2
# The correct answer is 1.414, proof? On Yt video: https://www.youtube.com/watch?v=Zz8AYQ8c5-U&t=251s
# Example 4: x^3 + 3*x - 2, x_a = 2, x_b = 1
# The correct answer is 0.596

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

x_a = float(input("Enter your x_a: "))
x_b = float(input("Enter your x_b: "))

prev_x_new = 0
i = 0

print()

more_than_20 = False

while True:

    i += 1
    print(f"Iteration {i}:")

    fx_a = equation.subs(x, x_a)
    fx_b = equation.subs(x, x_b)

    x_new = float(x_a - (fx_a * (x_a - x_b) / (fx_a - fx_b)))

    print("x_a - (f(x_a)(x_a - x_b) / (f(x_a) - f(x_b))")
    print(f"{shorten_deci(x_a)} - (({shorten_deci(fx_a)})({shorten_deci(x_a)} - {shorten_deci(x_b)}) / ({shorten_deci(fx_a)} - {shorten_deci(fx_b)}))")
    print(f" = {shorten_deci(x_new)} \n")

    if (round(x_new, 3) == round(prev_x_new, 3)):
        break
    elif i > 19:
        more_than_20 = True
        break

    x_a = x_new
    prev_x_new = x_new

if not more_than_20:
    print(f"Final answer: {round(x_new, 3)}\n")
else:
    print(f"Cannot find accurate answer but here ya go: {round(x_new, 3)}\n")