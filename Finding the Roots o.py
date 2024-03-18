import cmath

def quadratic_roots(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    return root1, root2

# Solve the quadratic equation: x^2 + 2x + 1 = 0
roots = quadratic_roots(1, 2, 1)
print("Root
