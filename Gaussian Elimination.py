import sympy as sp

# Define the symbols
x, y, z = sp.symbols("x y z")

"""Example # 1: Input these 3 equation:
    x + y - z = -2
    2*x - y + z = 5
    -x + 2*y + 2*z = 1
    The answer is on Yt video: https://www.youtube.com/watch?v=eDb6iugi6Uk&t=417s"""

""" !!! I didn't add 4 equations yet... only 3 equations so I need more time to study... !!! """

# Input the equations
equation_quantity = int(input("How many equation? "))

equations = []
for i in range(equation_quantity):
    equation_str = input(f"Enter equation {i+1}: ")
    eqlhs, eqrhs = equation_str.split("=")
    equation = sp.Eq(sp.sympify(eqlhs), sp.sympify(eqrhs))
    equations.append(equation)

#equations.append(sp.Eq(x + y - z, -2))
#equations.append(sp.Eq(2*x - y + z, 5))
#equations.append(sp.Eq(-x + 2*y + 2*z, 1))

# Extract coefficients and constants from the equations
coefficients = []
constants = []
for eq in equations:
    coefficients.append([eq.lhs.coeff(x), eq.lhs.coeff(y), eq.lhs.coeff(z)])
    constants.append(eq.rhs)

# Define the coefficient matrix and constant vector
A = sp.Matrix(coefficients)
B = sp.Matrix(constants)

# Combine the coefficient matrix and the constant vector into an augmented matrix
augmented_matrix = A.row_join(B)

# Print the augmented matrix
print("Augmented matrix: \n")
print(sp.pretty(augmented_matrix), "\n")

print("Add the row 2 + row 0 and then replace the answer on row 2:", "\n")

""" [row][column] """
for i in range(augmented_matrix.cols):
    augmented_matrix[2, i] += augmented_matrix[0, i]

print(sp.pretty(augmented_matrix), "\n")

# -(R:1, C:0)*R_0 + R_1
print("To become 0 on [Row 1, Column 0], you need to multiply opposite and then multiply by R_0 + R_1:", "\n")
want_zero = -augmented_matrix[1, 0]

for i in range(augmented_matrix.cols):
    augmented_matrix[1, i] += want_zero * augmented_matrix[0, i]

print(sp.pretty(augmented_matrix), "\n")

print("Add the row 2 + row 1 and then replace the answer on row 1:", "\n")
for i in range(augmented_matrix.cols):
    augmented_matrix[2, i] += augmented_matrix[1, i]

print(sp.pretty(augmented_matrix), "\n")

print("To become one on [Row 1, Column 1] and [Row 2, Column 2], you need to multiply it by itself with fraction from R_1 and R_2:", "\n")
want_one1 = 1/augmented_matrix[1, 1]
want_one2 = 1/augmented_matrix[2, 2]

# Start from row 1, column 1
for i in range(1, augmented_matrix.cols):
    augmented_matrix[1, i] *= want_one1

# Start from row 2, column 2
for i in range(2, augmented_matrix.cols):
    augmented_matrix[2, i] *= want_one2

print(sp.pretty(augmented_matrix), "\n")

# Extract coefficients and constants from the augmented matrix
coefficients = augmented_matrix[:, :-1]  # Exclude the last column
constants = augmented_matrix[:, -1]  # Last column

# Create equations from coefficients and constants with z
equations = []
equation = ""
for i in range(coefficients.rows):
    lhs = ""
    for j, var in enumerate([x, y, z]):
        if coefficients[i, j] != 0:
            if coefficients[i, j] == 1:
                lhs += f"{var}"
            else:
                lhs += f"{coefficients[i, j]}*{var}"
            if j < coefficients.cols - 1:
                lhs += " + "
    equations.append(f"{lhs} = {constants[i]}")

print("Row Echelon Form: \n")

y_constant = None
z_constant = None
x_equation = None
y_equation = None

# Print the equations
for equation in equations:
    eqlhs, eqrhs = equation.split("=")
    print(equation)
    if eqlhs.strip() == "z":
        z_constant = eqrhs.strip()
    elif "y" in eqlhs and "x" not in eqlhs:
        y_equation = equation
    elif "x" in eqlhs:
        x_equation = equation

# Show output solution, solving y equation
print(f"\n{y_equation}")
eqlhs, eqrhs = y_equation.split("=")
y_equation_str = str(y_equation)
y_equation_str = y_equation_str.replace("z", str(f"({z_constant})"))
print(y_equation_str)
y_equation = sp.Eq(sp.sympify(eqlhs), sp.sympify(eqrhs))
y_equation = sp.simplify(y_equation.subs(z, z_constant))
print(sp.pretty(y_equation))
y_constant = y_equation.rhs

# Show output solution, solving y equation
print(f"\n{x_equation}")
eqlhs, eqrhs = x_equation.split("=")
x_equation_str = str(x_equation)
x_equation_str = x_equation_str.replace("z", str(f"({z_constant})"))
x_equation_str = x_equation_str.replace("y", str(f"({y_constant})"))
print(x_equation_str)
x_equation = sp.Eq(sp.sympify(eqlhs), sp.sympify(eqrhs))
x_equation = x_equation.subs(z, z_constant)
x_equation = x_equation.subs(y, y_constant)
x_equation = sp.simplify(x_equation)
print(sp.pretty(x_equation))


