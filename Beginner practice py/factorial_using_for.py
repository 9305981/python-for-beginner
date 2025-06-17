# Find the factorial of a number using a for loop (not recursion).
def factorial(n):
    if n==0 or n==1:
        return n
    else:
        return n * factorial(n-1)

num=int(input("enter number"))
print("factorial" , factorial(num))
