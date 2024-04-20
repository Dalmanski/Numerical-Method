import sympy as sp

x = sp.symbols("x")

# Example 1: x^3 - 4*x^2 + 1 = 0
# The correct answer is 0.5374, proof? On Yt video: https://www.youtube.com/watch?v=-5e2cULI3H8

# Example 2: x^2 - x - 1 = 0
# The correct answer is 1.618, proof? On Yt video: https://www.youtube.com/watch?v=lN1JXolkKCM&t=121s

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

    f = float(equation.subs(x, x_i))
    f_d = float(derivative.subs(x, x_i))

    answer = float(x_i - (f / f_d))

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