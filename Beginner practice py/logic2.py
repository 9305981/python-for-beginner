# Check if a triangle is valid given 3 sides.
def is_valid_triangle(a, b, c):
    if a + b > c and a + c > b :
        if b + c > a:
            print(f"valid triangle")
    else:
        print(f"not a valid triangle")

a, b, c = map(int, input("Enter 3 sides of a triangle separated by space: ").split())

# Call the function
is_valid_triangle(a, b, c)