#Find the factorial of a number using recursion
def fac(n):
    if n==0 or n==1:
        return n
    else :
        return n * fac(n-1)
num=int(input("enter number"))
print("factorial",fac(num))