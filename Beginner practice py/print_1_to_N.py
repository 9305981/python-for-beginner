# Function to print all even numbers from 1 to n
def print_even_numbers(n):
    for i in range(2, n + 1, 2):
        print(i, end=' ')

num = int(input("Enter a number: "))
print_even_numbers(num)
