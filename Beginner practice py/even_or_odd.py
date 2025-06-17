# Take 3 numbers as input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
# Function to check even or odd
def check_even_odd(a, b, c):
    result = []

    for num in [a, b, c]:
        if num % 2 == 0:
            result.append(f"{num} is Even")
        else:
            result.append(f"{num} is Odd")
    
    return result

# Call the function and print result
output = check_even_odd(a, b, c)
for line in output:
    print(line)