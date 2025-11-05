# Swapping two numbers using arithmetic operations

# Take input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nBefore swapping:")
print(f"a = {a}, b = {b}")

# Swap using arithmetic operators
a = a + b
b = a - b
a = a - b 

print("\nAfter swapping:")
print(f"a = {a}, b = {b}")
