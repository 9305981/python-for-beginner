# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even ✅"
    else:
        return f"{num} is Odd ❌"

# Take input from user
n = int(input("Enter a number: "))

# Call the function and print result
result = check_even_odd(n)
print(result)