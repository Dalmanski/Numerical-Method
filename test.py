import sympy as sp

# Define the symbols
x, y, z = sp.symbols("x y z")

# Example augmented matrix
augmented_matrix = sp.Matrix([[1, 1, -2, -2]])

import sympy as sp

# Define the symbols
x, y, z = sp.symbols("x y z")

# Example equation
equation = x + 2*y - 3*z + 4

# Check if 'z' appears in the equation
if z in equation.free_symbols:
    # Extract the constant term of 'z'
    constant_term = equation.coeff(z, 0)
    print("The constant term of 'z' is:", constant_term)
else:
    print("The equation does not contain 'z'.")











