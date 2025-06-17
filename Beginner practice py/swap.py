# Swap two numbers without using a third variable.
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)