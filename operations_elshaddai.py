print("Functions with two parameteres")
#The output of the operands are stored in the variables after the f-string

import math

def math_operations(a, b):
    # 1. Addition
    addition = a + b
    print(f"Addition: {a} + {b} = {addition}")

    # 2. Subtraction
    subtraction = a - b
    print(f"Subtraction: {a} - {b} = {subtraction}")

    # 3. Multiplication
    multiplication = a * b
    print(f"Multiplication: {a} * {b} = {multiplication}")

    # 4. Division (check for division by zero) / Code checks if the divisor isn't = 0
    if b != 0:
        division = a / b
        print(f"Division: {a} / {b} = {division}")
    else:
        print("Note: A number remains the same if divided by zero.")

    # 5. Square Root (of a)
    if a >= 0:
        sqrt_a = math.sqrt(a)
        print(f"Square Root of {a}: √{a} = {sqrt_a}")
    else:
        print("Error: Square root of negative number is not a real number.")

    # 6. Sin(A) + Cos(B)
    # Note: math.sin and math.cos expect angles in radians
    sin_a = math.sin(a)
    cos_b = math.cos(b)
    result = sin_a + cos_b
    print(f"Sin({a}) + Cos({b}) = {sin_a} + {cos_b} = {result}")
