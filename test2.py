import sympy as sp

# Define the symbol
x, y = sp.symbols("x y")

# Define the expression
expression = ((x**2)+1)/((x**2)-1)

# Simplify the expression
simplified_expression = sp.diff(expression, x)
simplified_expression = sp.simplify(expression)

# Print the simplified expression
print(expression)
print("Simplified expression: \n", sp.pretty(simplified_expression))
