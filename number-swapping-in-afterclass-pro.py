# Swapping three numbers

# Getting inputs
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

print("\nBefore swapping:")
print(f"a = {a}, b = {b}, c = {c}")

# Swapping
a, b, c = c, a, b

print("\nAfter swapping:")
print(f"a = {a}, b = {b}, c = {c}")
