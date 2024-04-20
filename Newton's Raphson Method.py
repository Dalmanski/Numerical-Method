import sympy as sp

x = sp.symbols("x")

equation_str = input("Enter your equation: ")
equation_str = equation_str.replace("^", "**")

if "=" in equation_str:
    eqlhs, eqrhs = equation_str.split("=")
    equation_str = eqlhs

equation = sp.sympify(equation_str)

derivative = sp.diff(equation, x)

print(f"Derivative: {derivative} \n")

i = 0
x_i = 0.5

prev_answer = 0

while True:
    
    i += 1
    print(f"Iteration {i}: \n")

    f = equation.subs(x, x_i)
    f_d = derivative.subs(x, x_i)

    answer = x_i - (f / f_d)

    print("x_i - (f(x_i) / f_d(x_i))")
    print(f"{x_i} - (f({x_i}) / f'({x_i}))")
    print(f"f({x_i}) = {f}")
    print(f"f'({x_i}) = {f_d}")
    print(f"{answer}\n")

    if (round(answer, 3) == round(prev_answer, 3)):
        break

    prev_answer = answer
    x_i = answer

print(f"Final answer: {round(answer, 3)}")