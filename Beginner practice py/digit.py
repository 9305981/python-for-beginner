# Find the sum of digits of a given number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
# Test the function
num=int(input("enter number:"))
print(sum_of_digits(num))  # Output: 15
