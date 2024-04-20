import sympy as sp

x = sp.symbols("x")

# Example 1: x^2 - x - 1 = 0, x_a = 3, x_b = 2
# The correct answer is 1.618, proof? On Yt video: https://www.youtube.com/watch?v=AN6YxAoUqLM&t=435s
# Example 2: x^4 - x - 10, x_a = 1, x_b = 2
# The correct answer is 1.856, proof? On Yt video: https://www.youtube.com/watch?v=3g19OMfCpCA
# Example 3: x^2 - 2, x_a = 1, x_b= 2
# The correct answer is 1.414, proof? On Yt video: https://www.youtube.com/watch?v=Zz8AYQ8c5-U&t=251s

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

while True:

    i += 1
    print(f"Iteration {i}:")

    fx_a = equation.subs(x, x_a)
    fx_b = equation.subs(x, x_b)

    x_new = float(x_a - (fx_a * (x_a - x_b) / (fx_a - fx_b)))

    print("x_a - (f(x_a)(x_a - x_b) / (f(x_a) - f(x_b))")
    print(f"{x_a} - (({fx_a})({x_a} - {x_b}) / ({fx_a} - {fx_b}))")
    print(f"{x_new} \n")

    if (round(x_new, 3) == round(prev_x_new, 3)):
        break

    x_a = x_new
    prev_x_new = x_new

print(f"Final answer: {round(x_new, 3)}")