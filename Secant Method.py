import sympy as sp

x = sp.symbols("x")

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